from api.core import Mixin
from .base import db
from datetime import datetime


# Note that we use sqlite for our tests, so you can"t use Postgres Arrays
class Email(Mixin, db.Model):
    """Email Table."""

    __tablename__ = "robot_email"

    id = db.Column(db.BigInteger, unique=True, primary_key=True)
    email = db.Column(db.String, nullable=False)
    user_id = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return f"<Email {self.email}>"
