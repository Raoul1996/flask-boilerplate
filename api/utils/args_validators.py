from webargs import fields, validate

robot_put_args = {
    "robot_id": fields.Str(required=True, location="view_args"),
    "name": fields.Str(required=True, ),
    "description": fields.Str(required=True, ),
    "type": fields.Str(required=True, )
}
robot_post_args = {
    "name": fields.Str(required=True, ),
    "description": fields.Str(required=True, ),
    "type": fields.Str(required=True, )
}
register_args = {
    "name": fields.Str(required=True, validate=validate.Length(min=4)),
    "email": fields.Str(required=True, validate=validate.Email()),
    "password": fields.Str(required=True, validate=lambda p: len(p) >= 6),
}
login_args = {
    "email": fields.Str(required=True, validate=validate.Length(min=4)),
    "password": fields.Str(required=True, validate=lambda p: len(p) >= 6),
}

forget_args = {
    "email": fields.Str(required=True, validate=validate.Email()),
}

data_args = {
    "robot_id": fields.Str(required=True),
    "position_x": fields.Str(required=True),
    "position_y": fields.Str(required=True),
    "position_z": fields.Str(required=True),
    "velocity_x": fields.Str(required=True),
    "velocity_y": fields.Str(required=True),
    "velocity_z": fields.Str(required=True),
    "direction_x": fields.Str(required=True),
    "direction_y": fields.Str(required=True),
    "direction_z": fields.Str(required=True),
    "ip": fields.Str(required=True),
    "data": fields.Str(required=True),
}
list_args = {
    "page": fields.Str(required=False, missing="1", location="querystring"),
    "size": fields.Str(required=False, missing="20", location="querystring")
}
list_with_id_args = {
    "robot_id": fields.Str(required=True, location="view_args"),
    "page": fields.Str(required=False, missing="1", location="querystring"),
    "size": fields.Str(required=False, missing="20", location="querystring")
}
