from api.core import create_response, serialize_list
from api.models import Data, base
from api.views.auth import login_required
from api.utils.args_validators import data_args, list_with_id_args, list_args
from flask import (Blueprint)
from webargs.flaskparser import use_args

data = Blueprint("data", __name__, url_prefix="/api/v1/data")


@data.route("/add", methods=["POST"])
@login_required
@use_args(data_args)
def robot_data(args):
    robot_id = args["robot_id"]
    data_instance = Data(robot_id)
    data_instance.position_x = args["position_x"]
    data_instance.position_y = args["position_y"]
    data_instance.position_z = args["position_z"]
    data_instance.velocity_x = args["velocity_x"]
    data_instance.velocity_y = args["velocity_y"]
    data_instance.velocity_z = args["velocity_z"]
    data_instance.direction_x = args["direction_x"]
    data_instance.direction_y = args["direction_y"]
    data_instance.direction_z = args["direction_z"]
    data_instance.ip = args["ip"]
    data_instance.data = args["data"]
    try:
        base.db.session.add(data_instance)
        base.db.session.commit()
        return create_response(data=args, message="ok", code=0)
    except Exception:
        return create_response(data={}, message="error", code=9999)


@data.route("/list/<robot_id>", methods=["GET"])
@login_required
@use_args(list_with_id_args)
def robot_data_with_id_list(args, **kwargs):
    data_list_total_length = len(Data.query.filter_by(robot_id=args["robot_id"]).all())
    data_list = Data.query.filter_by(robot_id=args["robot_id"]).order_by(Data.create_time.desc()).paginate(
        page=int(args["page"]), per_page=int(args["size"]), error_out=False
    ).items
    if data_list:
        return create_response(data={
            "data": serialize_list(data_list),
            "total": data_list_total_length
        }, code=0)
    else:
        return create_response(data=[], code=5001, message="data is not exist")


@data.route("/list", methods=["GET"])
@login_required
@use_args(list_args)
def robot_data_list(args):
    data_list_total_length = len(Data.query.all())
    data_list = Data.query.order_by(Data.create_time.desc()).paginate(
        page=int(args["page"]), per_page=int(args["size"]), error_out=False
    ).items
    if data_list:
        return create_response(data={
            "data": serialize_list(data_list),
            "total": data_list_total_length
        }, code=0)
    else:
        return create_response(data=[], code=5001, message="data is not exist")
