from api.core import Mixin
from .base import db
from datetime import datetime


class User(Mixin, db.Model):
    """Person Table."""

    __tablename__ = "robot_user"

    id = db.Column(db.BigInteger, unique=True, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<User {self.name}>"
