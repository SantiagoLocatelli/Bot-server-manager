from http import HTTPStatus

from project.responses.response_constants import OK, STUDENT_NOT_FOUND, STUDENT_ALREADY_REGISTERED
from project.dao.student_dao import StudentDao
from project.utils.sql_connection import BaseSQLConnection
from project.model.student_model import Student, StudentState
from flask import current_app

def get_student_by_dni(dni):
    db_name = current_app.config.get('DB_NAME')
    with BaseSQLConnection(db_name) as base_dao:
        student_dao = StudentDao(base_dao.get_session())
        student = student_dao.get_student_by_identificador(dni)

        if not student:
            return STUDENT_NOT_FOUND, {}, HTTPStatus.NOT_FOUND

        return OK, student.to_dict(), HTTPStatus.OK

def register_student(identificador, discord_id):
    cantidad = 0
    cantidad_maxima = 5
    while cantidad < cantidad_maxima:
        try:
            db_name = current_app.config.get('DB_NAME')
            with BaseSQLConnection(db_name) as base_dao:
                student_dao = StudentDao(base_dao.get_session())
                student = student_dao.get_student_by_identificador(identificador)

                if not student:
                    return STUDENT_NOT_FOUND, {}, HTTPStatus.NOT_FOUND

                if student.registrado:
                    return STUDENT_ALREADY_REGISTERED, {}, HTTPStatus.BAD_REQUEST
                
                student.registrado = True
                student.discord_id = discord_id
                student_dao.session.commit()

                return OK, student.to_dict(), HTTPStatus.OK
        except:
            cantidad += 1


def get_students_by_states(states):
    db_name = current_app.config.get('DB_NAME')
    with BaseSQLConnection(db_name) as base_dao:
        student_dao = StudentDao(base_dao.get_session())
        students = student_dao.get_students_by_states(states)

        return OK, [s.to_dict() for s in students], HTTPStatus.OK
    
def loads_students(filename, cuatrimestre):
    estado = StudentState.CURSANDO.value
    with open(filename) as inscriptos:
        _headers = inscriptos.readline()   
        lines = inscriptos.readlines()
        print(lines)
        db_name = current_app.config.get('DB_NAME')
        with BaseSQLConnection(db_name) as base_dao:
            student_dao = StudentDao(base_dao.get_session())
            cantidad = 0
            for line in lines:
                student = line.strip('\n').split(',')
                student_dao.create_student(student[1], student[0], cuatrimestre, estado, False)
                print("Se inserto el alumno: ", student)
                cantidad += 1
            student_dao.session.commit()
            print(f"Se insertaron {cantidad} alumnos")

    return OK, {"message": f"Se insertaron {cantidad} alumnos"}, HTTPStatus.OK