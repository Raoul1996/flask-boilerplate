import functools
from datetime import datetime
import os
from flask import (Blueprint, g, session, render_template)
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import Forbidden
from webargs import fields, validate
from webargs.flaskparser import use_args

from api.core import create_response
from api.models import User
from api.models.base import db
from api.utils.mail import send_mail
from api.utils.token import generate_confirmation_token, confirm_token
from api.utils.args_validators import login_args, register_args, forget_args
from api import config

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return create_response(data={}, code=4001, message="need login")
        return view(**kwargs)

    return wrapped_view


def verify_email_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user and not g.user.status:
            return create_response(data={}, code=4002, message="need verify email address")
        return view(**kwargs)

    return wrapped_view


@auth.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()


@auth.route("/register", methods=["POST"])
@use_args(register_args, locations=("json",))
def register(args):
    """Register a new user.
    Validates that the name is not already taken. Hashes the
    password for security.
    """
    name = args["name"]
    email = args["email"]
    password = args["password"]
    user_exist = User.query.filter_by(email=email).first()
    if user_exist:
        return create_response(data={}, code=1001, message="email is already used.")
    else:
        user_instance = User(name=name)
        user_instance.password = generate_password_hash(password)
        user_instance.email = email
        try:
            db.session.add(user_instance)
            db.session.commit()
        except Exception:
            db.session.rollback()
        token = generate_confirmation_token(email)
        html = render_template("mail/register.html", ctx={"name": name, "token": token})
        print(html)
        send_mail(subject="Verify Email Address",
                  sender=config.get('base').MAIL_USERNAME,
                  recipients=[email],
                  html=html,
                  )
        return create_response(data={"name": name, "email": email}, message="send verify email successfully", code=0)


@auth.route("/login", methods=["POST"])
@use_args(login_args, locations=("json",))
def login(args):
    """Log in a registered user by adding the user id to the session."""
    email = args["email"]
    password = args["password"]
    error = None
    user = User.query.filter_by(email=email).first()
    if user is None:
        error = "Incorrect email."
    elif not check_password_hash(user.password, password):
        error = "Incorrect password."
    if error is None:
        # store the user id in a new session and return to the index
        session.clear()
        session["user_id"] = user.id
        return create_response(code=0, data=user.to_dict(["id", "name"]))
    else:
        return create_response(code=10002, message=error, data={})


@auth.route("/forget", methods=["PUT"])
@use_args(forget_args, locations=("json",))
def forget(args):
    email = args["email"]
    user_exist = User.query.filter_by(email=email).first()
    if user_exist:
        html = render_template("mail/reset.html", ctx={"name": user_exist.name})
        send_mail(subject="Password Reset",
                  sender=os.environ.get("qqmailaddress"),
                  recipients=[email],
                  html=html,
                  )
        return create_response(data={}, message="Send mail successfully", code=0, )
    return create_response(data={}, message="email is not current", code=1003)


@auth.route("/verify/<token>", methods=["GET"])
# @login_required
def verify_email(token):
    try:
        email = confirm_token(token)
    except Exception:
        raise Forbidden(description="The confirmation link is invalid or has expired.")
    if email:
        user = User.query.filter_by(email=email).first_or_404()
        if user.status:
            return create_response(data={}, message="Account already confirmed. Please login.", code=0)
        else:
            user.status = True
            user.update_time = datetime.now()
            db.session.add(user)
            db.session.commit()
            return create_response(data={}, message="Active email successfully", code=0)
    else:
        return create_response(data={}, message="email is not exist.",code=3001)


@auth.route("/profile", methods=["GET"])
@login_required
def profile():
    return create_response(data=g.user.to_dict(["id", "name", "email"]), code=0)


@auth.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return create_response(data={}, code=0)
