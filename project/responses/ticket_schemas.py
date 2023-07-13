from marshmallow import Schema, fields, validate, ValidationError

class Ticket(Schema):
        id = fields.Integer()
        description = fields.Str(validate=validate.Length(max=100))

