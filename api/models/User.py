from api.core import Mixin
from .base import db, TimestampMixin


class User(Mixin, TimestampMixin, db.Model):
    """User Table."""

    __tablename__ = "robot_user"

    id = db.Column(db.BigInteger, unique=True, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, nullable=False)
    college = db.Column(db.SMALLINT, nullable=False, default=2)
    password = db.Column(db.String, nullable=False)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<User {self.name}>"
