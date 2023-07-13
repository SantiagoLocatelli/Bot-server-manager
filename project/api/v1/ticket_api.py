from flask_apispec.views import MethodResource
from flask_restful import Resource
from project.utils.utils import log_endpoint, generate_response
from project.utils.utils import auth_required
from http import HTTPStatus
from project.responses.response_constants import OK
from project.service import ticket_service

class Ticket(Resource, MethodResource):
    # @auth_required()
    @log_endpoint
    def get(self, ticketId):

        response = ticket_service.get_ticket_by_id(ticketId)
        return generate_response(OK, response, HTTPStatus.OK)
    