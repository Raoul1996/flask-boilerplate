from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# instantiate database object
db = SQLAlchemy()


class TimestampMixin(object):
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)
