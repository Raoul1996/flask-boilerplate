import functools
from api.core import create_response
from api.models import User
from flask import (Blueprint, flash, g, request, session)
from werkzeug.security import check_password_hash, generate_password_hash

from api.models.base import db

auth = Blueprint("auth", __name__, url_prefix="/auth")


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return create_response(data={},code=4001,message="need login")
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
def register():
    """Register a new user.
    Validates that the name is not already taken. Hashes the
    password for security.
    """
    if request.method == "POST":
        name = request.json["name"]
        email = request.json["email"]
        password = request.json["password"]
        error = None

        if not name:
            error = "Name is required."
        elif not password:
            error = "Password is required."
        elif not email:
            error = "Email is required."
        if error is None:
            is_exist = User.query.filter_by(name=name).first()
            if is_exist:
                return create_response(data={}, code=1001, message="user exists")
            user = User(name=name)
            user.password = generate_password_hash(password)
            user.email = email
            db.session.add(user)
            db.session.commit()
            return create_response(data={"name": name, "email": email}, code=0)
        else:
            return create_response(data={},code=9000,message=error)
        flash(error)

    return create_response(data={}, message="unknown error", code=5001)


@auth.route("/login", methods=["POST"])
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        name = request.json["name"]
        password = request.json["password"]
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
            return create_response(code=10002, message=error)

    return create_response(data={}, message="unknown error", code=5001)


@auth.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return create_response(data={}, code=0)
