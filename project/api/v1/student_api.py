from flask_apispec.views import MethodResource
from flask_restful import Resource
from project.utils.utils import log_endpoint, generate_response
from http import HTTPStatus
from project.responses.response_constants import OK
from project.service import student_service
from flask_apispec import use_kwargs, marshal_with
from webargs import fields
from project.model.student_model import StudentState

class Student(Resource, MethodResource):

    @log_endpoint
    @use_kwargs({'dni': fields.Str(required=True)}, location=('query'))
    def get(self, dni):
        code, response, code_http = student_service.get_student_by_dni(dni)
        return generate_response(code, response, code_http)
    

class Students(Resource, MethodResource):
    @log_endpoint
    @use_kwargs({'filename': fields.Str(required=True), 'cuatrimestre': fields.Integer(required=True)}, location=('json'))
    def post(self, filename, cuatrimestre):
        code, response, code_http = student_service.loads_students(filename, cuatrimestre)
        return generate_response(code, response, code_http)

class RegisterStudent(Resource, MethodResource):
    @log_endpoint
    @use_kwargs({'discord_id': fields.Str(required=True),
                 'identificador': fields.Str(required=True)}, location=('json'))
    def put(self, identificador, discord_id):
        code, response, code_http = student_service.register_student(identificador, discord_id)
        return generate_response(code, response, code_http)
    
class ApprovedStudents(Resource, MethodResource):
    @log_endpoint
    def get(self):
        code, response, code_http = student_service.get_students_by_states([StudentState.APROBADO.value])
        return generate_response(code, response, code_http)