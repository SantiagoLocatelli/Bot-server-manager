from http import HTTPStatus

from project.responses.response_constants import OK
from project.dao.student_dao import StudentDao
from project.utils.sql_connection import BaseSQLConnection

def get_student_by_dni(dni):

    with BaseSQLConnection("pensamiento_computacional") as base_dao:
        student_dao = StudentDao(base_dao.get_session())
        student = student_dao.get_student_by_dni(dni)

        return student.to_dict()
