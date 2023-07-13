from http import HTTPStatus

from project.responses.response_constants import OK
from project.dao.ticket_dao import TicketDao
from project.utils.sql_connection import BaseSQLConnection

def get_ticket_by_id(id):

    with BaseSQLConnection("main") as base_dao:
        ticket_dao = TicketDao(base_dao.get_session())
        ticket = ticket_dao.get_ticket_by_id(id)

        return ticket
