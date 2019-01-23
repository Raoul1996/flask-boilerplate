from api.core import Mixin
from .base import db,TimestampMixin


class Robot(Mixin, TimestampMixin,db.Model):
    __tablename__ = "robot_robot"

    id = db.Column(db.BigInteger, unique=True, primary_key=True)
    description = db.Column(db.Text, default="")
    name = db.Column(db.String, unique=True, nullable=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    type = db.Column(db.String, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Robot {self.name}>"
