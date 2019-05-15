from api.core import Mixin
from .base import db, TimestampMixin


class Robot(Mixin, db.Model, TimestampMixin):
    __tablename__ = "robot_robot"

    id = db.Column(db.BigInteger, unique=True, primary_key=True)
    description = db.Column(db.Text, default="")
    name = db.Column(db.String(100), unique=True, nullable=True)
    owner_id = db.Column(db.BigInteger, nullable=False)
    type = db.Column(db.String(4), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Robot {}>".format(self.name)
