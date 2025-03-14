import os
import traceback
from multiprocessing import Manager
from flask import Flask, jsonify, request
from flask_apispec.extension import FlaskApiSpec
from flask_cors import CORS
from flask_restful import Api
from log import LOG
from project.api.v1.student_api import Student, RegisterStudent, ApprovedStudents, Students

manager_dict = Manager().dict()

def _register_blueprints(api, api_spec):
    api.add_resource(Student, '/v1/student')
    api_spec.register(Student)
    api.add_resource(RegisterStudent, '/v1/student/register')
    api_spec.register(RegisterStudent)
    api.add_resource(ApprovedStudents, '/v1/student/approved')
    api_spec.register(ApprovedStudents)
    api.add_resource(Students, '/v1/students')
    api_spec.register(Students)


def _runtime_error_handler(e):
    LOG.error(traceback.format_exc())
    return jsonify({'code': 'CCOD000', 'desc': str(e)}), 500


def _http_error_handler(e):
    LOG.error("Error response code {}. Detail {}".format(e.code, e.description))
    return jsonify(e.description), e.code


def _register_error_handlers(app):
    app.register_error_handler(400, _http_error_handler)
    app.register_error_handler(401, _http_error_handler)
    app.register_error_handler(403, _http_error_handler)
    app.register_error_handler(404, _http_error_handler)
    app.register_error_handler(409, _http_error_handler)
    app.register_error_handler(500, _runtime_error_handler)
    app.register_error_handler(Exception, _runtime_error_handler)


def after_request(response):
    # This avoids the duplication of registry in the log,
    # since that 500 is already logged via @app.errorhandler.
    LOG.info('{} {} - status: {}'.format(request.method, request.full_path, response.status))
    return response


def init_app():
    application = Flask(__name__)
    env = os.environ.get('ENV', 'local')
    if env == 'prod':
        application.config.from_object("project.config.ProdConfig")
    elif env == 'dev':
        application.config.from_object("project.config.DevConfig")
    else:
        application.config.from_object("project.config.LocalConfig")

    application.after_request(after_request)
    api = Api(application)
    api_spec = FlaskApiSpec(application)
    _register_blueprints(api, api_spec)
    _register_error_handlers(application)
    application.config.update({'manager_dict': manager_dict})
    CORS(application,resources={r"/*":{"origins":"*"}})
    return application

app = init_app()

@app.route("/")
def health_check():
    return jsonify(status="ok")
