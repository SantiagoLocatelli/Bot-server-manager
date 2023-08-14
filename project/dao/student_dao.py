from project.model.student_model import Student, StudentState
from project.utils.sql_connection import BaseDao

class StudentDao(BaseDao):

    def get_student_by_dni(self, dni):

        student = self.session.query(Student) \
            .filter(Student.cuit == dni).first()

        return student
    
    def get_students_by_states(self, states):
        students = self.session.query(Student) \
            .filter(Student.estado.in_(states)).all()
        
        return students

    def create_student(self, cuit, nombre, cuatrimestre_id, estado=StudentState.CURSANDO.value, registrado=False, discord_id=None):
        student = Student(cuit, nombre, cuatrimestre_id, registrado, estado, discord_id)
        self.session.add(student)
        return student
    
