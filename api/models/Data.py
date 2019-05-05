from api.core import Mixin
from .base import db, TimestampMixin


class Data(Mixin, db.Model, TimestampMixin):
    __tablename__ = "robot_data"

    id = db.Column(db.BigInteger, unique=True, primary_key=True)
    robot_id = db.Column(db.BigInteger, nullable=False)
    position_x = db.Column(db.String(255), default=0)
    position_y = db.Column(db.String(255), default=0)
    position_z = db.Column(db.String(255), default=0)
    velocity_x = db.Column(db.String(255), default=0)
    velocity_y = db.Column(db.String(255), default=0)
    velocity_z = db.Column(db.String(255), default=0)
    direction_x = db.Column(db.String(255), default=0)
    direction_y = db.Column(db.String(255), default=0)
    direction_z = db.Column(db.String(255), default=0)
    battery = db.Column(db.Integer, default=100)
    temperature = db.Column(db.Integer, default=0)
    ip = db.Column(db.String(16), default="")
    data = db.Column(db.Text, default="")

    def __init__(self, robot_id):
        self.robot_id = robot_id

    def __repr__(self):
        return "<Data {}>".format(self.robot_id)
