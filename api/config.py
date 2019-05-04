"""
This file holds Configuration options. The Development config looks for a creds.ini file or defaults to the normal url.
DockerDevConfig is used when the env variable FLASK_ENV=docker, which is currently used in Dockerfile-dev and thus,
docker-compose. Production is used in Heroku as well as Zeit now. You may change these however you want.

DO NOT HARD CODE YOUR PRODUCTION URLS EVER. Either use creds.ini or use environment variables.
"""
import os
from api.core import get_db_url, get_email_conf


# more configuration options here http://flask.pocoo.org/docs/1.0/config/
class Config:
    SECRET_KEY = "testkey"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = "api.log"
    SECURITY_PASSWORD_SALT = "neuq"


class DevelopmentConfig(Config):
    url = (
        get_db_url()
        if get_db_url()
        else "mysql+pymysql://test_user:test_password@127.0.0.1/test"
    )
    SQLALCHEMY_DATABASE_URI = url
    SQLALCHEMY_ECHO = True
    DEBUG = True
    MAIL_SERVER = "smtp.qq.com"
    MAIL_PORT = 465
    MAIL_USERNAME = get_email_conf()["address"]
    MAIL_PASSWORD = get_email_conf()["pwd"]
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    )  # you may do the same as the development config
    DEBUG = False


class DockerDevConfig(Config):
    SQLALCHEMY_DATABASE_URI = get_db_url()
    DEBUG = True


config = {"base": Config, "dev": DevelopmentConfig, "prod": ProductionConfig, "docker": DockerDevConfig}
