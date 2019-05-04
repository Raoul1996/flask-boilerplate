from api.core import Mixin
from .base import db,TimestampMixin


# Note that we use sqlite for our tests, so you can't use Postgres Arrays
class Email(Mixin,db.Model, TimestampMixin):
    """Email Table."""

    __tablename__ = "robot_email"

    id = db.Column(db.BigInteger, unique=True, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.BigInteger, nullable=False)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return "<Email {}>".format(self.email)
