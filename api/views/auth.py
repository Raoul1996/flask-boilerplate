import functools
from api.core import create_response
from api.models import User
from flask import (Blueprint, flash, g, request, session)
from werkzeug.security import check_password_hash, generate_password_hash
from api.models.base import db
from webargs import fields
from webargs.flaskparser import use_args

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")

register_args = {
    "name": fields.Str(required=True),
    "email": fields.Str(required=True),
    "password": fields.Str(required=True)
}
login_args = {
    "name": fields.Str(required=True),
    "password": fields.Str(required=True)
}


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return create_response(data={}, code=4001, message="need login")
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
@use_args(register_args)
def register(args):
    """Register a new user.
    Validates that the name is not already taken. Hashes the
    password for security.
    """
    if request.method == "POST":
        name = args["name"]
        email = args["email"]
        password = args["password"]
        is_exist = User.query.filter_by(name=name).first()
        if is_exist:
            return create_response(data={}, code=1001, message="user exists")
        user = User(name=name)
        user.password = generate_password_hash(password)
        user.email = email
        db.session.add(user)
        db.session.commit()
        return create_response(data={"name": name, "email": email}, code=0)
    return create_response(data={}, message="unknown error", code=5001)


@auth.route("/login", methods=["POST"])
@use_args(login_args)
def login(args):
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        name = args["name"]
        password = args["password"]
        error = None
        user = User.query.filter_by(name=name).first()
        if user is None:
            error = "Incorrect name."
        elif not check_password_hash(user.password, password):
            error = "Incorrect password."
        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session["user_id"] = user.id
            return create_response(code=0, data=user.to_dict(["id", "name"]))
        else:
            return create_response(code=10002, message=error, data={})

    return create_response(data={}, message="unknown error", code=5001)


@auth.route("/profile", methods=["GET"])
@login_required
def profile():
    return create_response(data=g.user.to_dict(['id', 'name', 'email']))


@auth.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return create_response(data={}, code=0)
