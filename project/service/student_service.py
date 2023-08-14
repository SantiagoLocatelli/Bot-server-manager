from http import HTTPStatus

from project.responses.response_constants import OK, STUDENT_NOT_FOUND, STUDENT_ALREADY_REGISTERED
from project.dao.student_dao import StudentDao
from project.utils.sql_connection import BaseSQLConnection
from project.model.student_model import Student, StudentState

def get_student_by_dni(dni):

    with BaseSQLConnection("pensamiento_computacional") as base_dao:
        student_dao = StudentDao(base_dao.get_session())
        student = student_dao.get_student_by_dni(dni)

        if not student:
            return STUDENT_NOT_FOUND, {}, HTTPStatus.NOT_FOUND

        return OK, student.to_dict(), HTTPStatus.OK

def register_student(dni, discord_id):
    with BaseSQLConnection("pensamiento_computacional") as base_dao:
        student_dao = StudentDao(base_dao.get_session())
        student = student_dao.get_student_by_dni(dni)

        if not student:
            return STUDENT_NOT_FOUND, {}, HTTPStatus.NOT_FOUND

        if student.registrado:
            return STUDENT_ALREADY_REGISTERED, {}, HTTPStatus.BAD_REQUEST
        
        student.registrado = True
        student.discord_id = discord_id
        student_dao.session.commit()

        return OK, student.to_dict(), HTTPStatus.OK
    
def get_students_by_states(states):
    with BaseSQLConnection("pensamiento_computacional") as base_dao:
        student_dao = StudentDao(base_dao.get_session())
        students = student_dao.get_students_by_states(states)

        return OK, [s.to_dict() for s in students], HTTPStatus.OK
    
def loads_students(filename, cuatrimestre):
    estado = StudentState.CURSANDO.value
    source = 'project/db/2023 2C/'
    with open(f"{source}{filename}") as inscriptos:
        _headers = inscriptos.readline()   
        lines = inscriptos.readlines()
        print(lines)
        with BaseSQLConnection("pensamiento_computacional") as base_dao:
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