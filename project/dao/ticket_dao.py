from project.model.ticket_model import Ticket
from project.utils.sql_connection import BaseDao

class TicketDao(BaseDao):

    def get_ticket_by_id(self, id):

        ticket = self.session.query(Ticket) \
            .filter(Ticket.id == id).first()

        return ticket.to_dict()
    