from project.model.student_model import Student
from project.utils.sql_connection import BaseDao

class StudentDao(BaseDao):

    def get_student_by_dni(self, dni):

        student = self.session.query(Student) \
            .filter(Student.DNI == dni).first()

        return student
    
    def get_students_by_states(self, states):
        students = self.session.query(Student) \
            .filter(Student.estado.in_(states)).all()
        
        return students

    
