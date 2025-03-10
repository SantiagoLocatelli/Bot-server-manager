from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class DevConfig:
    ENV = "dev"
    POSTGRES_USER = "root"
    POSTGRES_PASSWORD = "admin"
    POSTGRES_IP = "localhost"
    POSTGRES_PORT = "3306"
    APISPEC_SWAGGER_URL = '/swagger/'
    APISPEC_SWAGGER_UI_URL = '/swagger-ui/'
    THIS_URL = "http://0.0.0.0:5001"
    DB_NAME = 's101170_PensamientoComputacional'

class LocalConfig:
    ENV = "local"
    POSTGRES_USER = "root"
    POSTGRES_IP = "localhost"
    POSTGRES_PORT = "3306"
    POSTGRES_PASSWORD = "admin"
    THIS_URL = "http://0.0.0.0:5001"
    DB_NAME = 's101170_PensamientoComputacional'

class ProdConfig:
    ENV = "prod"
    POSTGRES_USER = "u101170_FUwsSHLLAZ"
    POSTGRES_IP = "db-fde-02.sparkedhost.us"
    POSTGRES_PASSWORD = "8ABhJk7uTxsig9Bo.1S!adG3"
    POSTGRES_PORT = "3306"
    APISPEC_SWAGGER_URL = '/swagger/'
    APISPEC_SWAGGER_UI_URL = '/swagger-ui/'
    DB_NAME = 's101170_PensamientoComputacional'
