from api.core import Mixin
from datetime import datetime
from .base import db


class Data(Mixin, db.Model):
    __tablename__ = "robot_data"
    id = db.Column(db.BigInteger, unique=True, primary_key=True)
    robot_id = db.Column(db.BigInteger, nullable=False)
    x = db.Column(db.String, default="")
    y = db.Column(db.String, default="")
    z = db.Column(db.String, default="")
    ip = db.Column(db.String, default="")
    data = db.Column(db.Text, default="")
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)
