from api.core import create_response, serialize_list
from api.models import Robot
from flask import (Blueprint, flash, g, request)
from api.models.base import db
from api.views.auth import login_required
from webargs import fields
from webargs.flaskparser import use_args

robot = Blueprint("robot", __name__, url_prefix="/api/v1/robot")

robot_args = {
    "name": fields.Str(required=True),
    "description": fields.Str(required=True),
    "type": fields.Str(required=True)
}


@robot.route("", methods=["POST"])
@login_required
@use_args(robot_args)
def robot_create(args):
    name = args["name"]
    description = args["description"]
    user_id = g.user.id
    robot_type = args["type"]
    is_exist = Robot.query.filter_by(name=name).first()
    if is_exist:
        return create_response(data={}, code=2001, message="robot exists")
    else:
        robot_instance = Robot(name=name)
        robot_instance.description = description
        robot_instance.type = robot_type
        robot_instance.user_id = user_id
        db.session.add(robot_instance)
        db.session.commit()
        return create_response(data=args, code=0)
    flash(error)


@robot.route("/list", methods=["GET"])
@login_required
def robot_list():
    robots = Robot.query.all()
    error = None
    if not error:
        return create_response(data=serialize_list(robots, ["name", "type"]), code=0)
    else:
        return create_response(data={}, code=5001, message="unknown error")


@robot.route("/<int:robot_id>", methods=["GET", "PUT"])
@login_required
def single_robot(robot_id):
    robot_instance = Robot.query.filter_by(id=robot_id).first()
    return create_response(data=robot_instance.to_dict(["name", "type", "create_times"]), code=0)
