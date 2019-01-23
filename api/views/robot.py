from api.core import create_response, serialize_list
from api.models import Robot
from flask import (Blueprint, flash, g, request)
from api.models.base import db
from api.views.auth import login_required

robot = Blueprint("robot", __name__, url_prefix="/api/v1/robot")


@robot.route("", methods=["POST"])
@login_required
def robot_create():
    name = request.json["name"]
    description = request.json["description"]
    user_id = g.user.id
    robot_type = request.json["type"]
    is_exist = Robot.query.filter_by(name=name).first()
    error = None
    if name is None:
        error = 'Name is required.'
    if description is None:
        error = 'Description is required.'
    if robot_type is None:
        error = 'Robot type is required.'
    if not error:
        if is_exist:
            return create_response(data={}, code=2001, message="robot exists")
        else:
            robot_instance = Robot(name=name)
            robot_instance.description = description
            robot_instance.type = robot_type
            robot_instance.user_id = user_id
            db.session.add(robot_instance)
            db.session.commit()
            print(user_id)
            return create_response(data={
                "name": name,
                "description": description,
                "type": robot_type
            }, code=0)
    else:
        return create_response(data={}, code=9000, message=error)
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
    return create_response(data=robot_instance.to_dict(["name","type","create_times"]), code=0)
