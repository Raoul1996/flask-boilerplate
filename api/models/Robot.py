from api.core import Mixin
from datetime import datetime
from .base import db


class Robot(Mixin, db.Model):
    __tablename__ = "robot_robot"

    id = db.Column(db.BigInteger, unique=True, primary_key=True)
    description = db.Column(db.Text, default="")
    name = db.Column(db.String, unique=True, nullable=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    type = db.Column(db.String, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Robot {self.name}>"
