from sqlalchemy import INTEGER, VARCHAR, BOOLEAN, DATETIME, Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql import func
from project.model.base import Base

class Ticket(Base):
    __tablename__ = 'ticket'
    id = Column(INTEGER, nullable=False, primary_key=True, autoincrement=True)
    description = Column(VARCHAR(100), nullable=False)
    title = Column(VARCHAR(100), nullable=False)
    state = Column(INTEGER, nullable=False)

    def __init__(self, id, description, title, state):
        self.id = id
        self.description = description
        self.title = title
        self.state = state

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'title': self.title,
            'state': self.state,
        }
