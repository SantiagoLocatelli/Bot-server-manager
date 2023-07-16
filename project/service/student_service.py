from http import HTTPStatus

from project.responses.response_constants import OK, STUDENT_NOT_FOUND, STUDENT_ALREADY_REGISTERED
from project.dao.student_dao import StudentDao
from project.utils.sql_connection import BaseSQLConnection

def get_student_by_dni(dni):

    with BaseSQLConnection("pensamiento_computacional") as base_dao:
        student_dao = StudentDao(base_dao.get_session())
        student = student_dao.get_student_by_dni(dni)

        if not student:
            return STUDENT_NOT_FOUND, {}, HTTPStatus.NOT_FOUND

        return OK, student.to_dict(), HTTPStatus.OK

def register_student(dni):
    with BaseSQLConnection("pensamiento_computacional") as base_dao:
        student_dao = StudentDao(base_dao.get_session())
        student = student_dao.get_student_by_dni(dni)

        if not student:
            return STUDENT_NOT_FOUND, {}, HTTPStatus.NOT_FOUND

        if student.registrado:
            return STUDENT_ALREADY_REGISTERED, {}, HTTPStatus.BAD_REQUEST
        
        student.registrado = True
        student_dao.session.commit()

        return OK, student.to_dict(), HTTPStatus.OK

