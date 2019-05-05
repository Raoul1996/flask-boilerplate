import configparser
import logging
from typing import Tuple, List
from werkzeug.exceptions import InternalServerError
from werkzeug.local import LocalProxy
from flask import current_app, jsonify
from flask.wrappers import Response

# logger object for all views to use
logger = LocalProxy(lambda: current_app.logger)
core_logger = logging.getLogger("core")


def datetime_to_str(date_time, fmt="%Y-%m-%d %H:%M:%S"):
    datetime_str = date_time.strftime(fmt)
    return datetime_str


class Mixin:
    """Utility Base Class for SQLAlchemy Models.

    Adds `to_dict()` to easily serialize objects to dictionaries.
    """

    def to_dict(self, keys=None):
        if not keys:
            keys = self.__dict__.keys()
        data_dict = dict()
        items = dir(self)
        for key in keys:
            if key in items:
                val = getattr(self, key)
                if key in ("create_time", "modify_time","update_time"):
                    val = datetime_to_str(val)
                data_dict[key] = val
        data_dict.pop("_sa_instance_state", None)
        return data_dict
    # def to_dict(self) -> dict:
    #     d_out = dict((key, val) for key, val in self.__dict__.items())
    #     d_out.pop("_sa_instance_state", None)
    #     return d_out


def create_response(
        data: dict or list = None,
        status: int = 200,
        message: str = "",
        code: int = 5001,
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.

    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there"s only 2 values
    - make message a single string since we will only use one message per response

    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :param code <int> optional code
    :returns tuple of Flask Response and int
    """
    if type(data) is not dict and type(data) is not list and data is not None:
        logging.error(data)
        raise InternalServerError(description="Data should be a dictionary 😞")
    success = 200 <= status < 300
    if success:
        response = {"code": code, "success": success, "message": message, "data": data}
    else:
        response = {"code": -1, "success": success, "message": message, "data": data}
    return jsonify(response), status


def serialize_list(items: List, keys=None) -> List:
    """Serializes a list of SQLAlchemy Objects, exposing their attributes.

    :param items - List of Objects that inherit from Mixin
    :param keys - json keys
    :returns List of dictionaries
    """
    if not items or items is None:
        return []
    return [x.to_dict(keys) for x in items]


# add specific Exception handlers before this, if needed
# More info at http://flask.pocoo.org/docs/1.0/patterns/apierrors/
def all_exception_handler(error) -> Tuple[Response, int]:
    """Catches and handles all exceptions, add more specific error Handlers.
    :param error
    :returns Tuple of a Flask Response and int
    """
    logging.error(error)
    if hasattr(error, "code"):
        if error.code == 422:
            return create_response(message=str(error.description), data=error.data["messages"], status=int(error.code))
        elif hasattr(error, "description"):
            return create_response(message=str(error.description), data={}, status=int(error.code or 500))
    return create_response(message="unknown error", status=500)


def get_db_url(file: str = "creds.ini") -> str:
    """Gets Postgres URL including credentials from specified file.

    Example of File:
    ```
    [pg_creds]
    pg_url = postgresql://testusr:password@127.0.0.1:5432/testdb
    ```
    :param file name
    :returns str or None if exception failed
    """
    try:

        config = configparser.ConfigParser()
        config.read(file)

        mongo_section = config["db"]
        return mongo_section["db_url"]
    except KeyError:
        print("Failed to retrieve database url. Check if {} exists".format(file))
        return ''


def get_email_conf(file: str = 'creds.ini') -> dict:
    try:
        config = configparser.ConfigParser()
        config.read(file)

        email_sction = config["email"]
        return email_sction
    except KeyError:
        print("Failed to retrieve email. Check if {} exists".format(file))
        return {}
