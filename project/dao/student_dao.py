from project.model.student_model import Student
from project.utils.sql_connection import BaseDao

class StudentDao(BaseDao):

    def get_student_by_dni(self, dni):

        student = self.session.query(Student) \
            .filter(Student.DNI == dni).first()

        return student
    