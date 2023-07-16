from sqlalchemy import INTEGER, VARCHAR, BOOLEAN, DATETIME, Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql import func
from project.model.base import Base
from sqlalchemy.orm import relationship
import enum

class StudentState(enum.Enum):
    CURSANDO = 1
    APROBADO = 2
    DESAPROBADO = 3

class Period(Base):
    __tablename__ = "cuatrimestre"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    description = Column(VARCHAR(50), nullable=False)


    def __init__(self, description):
        self.description = description

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
        }

class Student(Base):
    __tablename__ = 'alumno'
    DNI = Column(INTEGER, nullable=False, primary_key=True)
    nombre = Column(VARCHAR(100), nullable=False)
    discord_id = Column(VARCHAR(30))
    cuatrimestre_id = Column(INTEGER, ForeignKey("cuatrimestre.id"), nullable=False)
    registrado = Column(BOOLEAN, default=False)
    cuatrimestre = relationship("Period", uselist=False)
    estado = Column(INTEGER, default=StudentState.CURSANDO.value)

    def __init__(self, DNI, nombre, cuatrimestre, registrado, estado=None, discord_id=None):
        self.DNI = DNI
        self.nombre = nombre
        self.cuatrimestre = cuatrimestre
        self.registrado = registrado
        self.estado = estado
        self.discord_id = discord_id

    def to_dict(self):
        return {
            'DNI': self.DNI,
            'nombre': self.nombre,
            'discord_id': self.discord_id,
            'cuatrimestre': self.cuatrimestre.to_dict(),
            'registrado': self.registrado,
            'estado': self.estado,
            'discord_id': self.discord_id,
        }
