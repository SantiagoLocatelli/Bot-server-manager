from flask_apispec.views import MethodResource
from flask_restful import Resource
from project.utils.utils import log_endpoint, generate_response
from http import HTTPStatus
from project.responses.response_constants import OK
from project.service import student_service
from flask_apispec import use_kwargs, marshal_with
from webargs import fields

class Student(Resource, MethodResource):

    @log_endpoint
    @use_kwargs({'dni': fields.Str(required=True)}, location=('query'))
    def get(self, dni):

        code, response, code_http = student_service.get_student_by_dni(dni)
        return generate_response(code, response, code_http)
    

class RegisterStudent(Resource, MethodResource):
    @log_endpoint
    def put(self, dni):
        code, response, code_http = student_service.register_student(dni)
        return generate_response(code, response, code_http)