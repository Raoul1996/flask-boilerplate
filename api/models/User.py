from api.core import Mixin
from .base import db, TimestampMixin


class User(Mixin, db.Model, TimestampMixin):
    """User Table."""

    __tablename__ = "robot_user"

    id = db.Column(db.BigInteger, unique=True, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    college = db.Column(db.SMALLINT, nullable=False, default=2)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return "<User {}>".format(self.name)
