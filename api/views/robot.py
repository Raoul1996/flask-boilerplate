from datetime import datetime
from api.core import create_response, serialize_list
from api.models import Robot
from flask import (Blueprint, g)
from api.models.base import db
from api.views.auth import login_required
from api.utils.args_validators import list_args, robot_post_args, robot_put_args
from webargs.flaskparser import use_args

robot = Blueprint("robot", __name__, url_prefix="/api/v1/robot")


@robot.route("/create", methods=["POST"])
@login_required
@use_args(robot_post_args)
def robot_create(args):
    name = args["name"]
    is_exist = Robot.query.filter_by(name=name).first()
    if is_exist:
        return create_response(data={}, code=2001, message="robot exists")
    else:
        robot_instance = Robot(name=name)
        robot_instance.description = args["description"]
        robot_instance.type = args["type"]
        robot_instance.owner_id = g.user.id
        db.session.add(robot_instance)
        db.session.commit()
        return create_response(data=Robot.query.filter_by(name=name).first().to_dict(), code=0)


@robot.route("/list", methods=["GET"])
@login_required
@use_args(list_args)
def get_list(args):
    robot_list_total_length = len(Robot.query.all())
    robot_list = Robot.query.order_by(Robot.create_time.desc()).paginate(
        page=int(args["page"]), per_page=int(args["size"]), error_out=False
    ).items
    if robot_list:
        return create_response(
            data={
                "data": serialize_list(robot_list),
                "total": robot_list_total_length},
            code=0, )
    else:
        return create_response(data={}, code=3001, message="data is not exist")


# must use the `**kwargs` to support view_args.
# https://webargs.readthedocs.io/en/latest/framework_support.html#url-matches
@robot.route("/<robot_id>", methods=["PUT"])
@login_required
@use_args(robot_put_args)
def single_robot(args, **kwargs):
    robot_instance = Robot.query.filter_by(id=args["robot_id"]).first()
    if robot_instance:
        robot_instance.name = args["name"]
        robot_instance.description = args["description"]
        robot_instance.type = args["type"]
        robot_instance.update_time = datetime.now()
        db.session.commit()
        return create_response(
            data=robot_instance.to_dict(),
            code=0)
    else:
        return create_response(data={}, message="robot is not exist.", code=3001)


@robot.route("/<int:robot_id>", methods=["GET"])
@login_required
def get_single_robot(robot_id):
    robot_instance = Robot.query.filter_by(id=robot_id).first()
    if robot_instance:
        return create_response(
            data=robot_instance.to_dict(),
            code=0)
    else:
        return create_response(data={}, message="robot is not exist.", code=3001)


@robot.route("/<int:robot_id>", methods=["PATCH"])
@login_required
def delete_robot_by_id(robot_id):
    robot_instance = Robot.query.filter_by(id=robot_id).first()
    if robot_instance:
        print(g.user)
        if g.user.id == robot_instance.owner_id:
            robot_instance.is_deleted = True
            robot_instance.update_time = datetime.now()
            db.session.commit()
            return create_response(data=robot_instance.to_dict(), code=0)
        else:
            return create_response(data={}, message="permission denied,only owner can delete their own robot.",
                                   code=4003)
    else:
        return create_response(data={}, message="robot is not exist.", code=3001)
