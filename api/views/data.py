import functools
from api.core import create_response, serialize_list
from api.models import Data
from api.views.auth import login_required
from flask import (Blueprint, flash, g, request, session)

auth = Blueprint("data", __name__, url_prefix="/api/v1/data")


@auth.route('/list', methods=["GET"])
@login_required
def robot_data_list():
    data_list = Data.query.all()
    return create_response(data=serialize_list(data_list), code=0)
