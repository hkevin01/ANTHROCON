from marshmallow import Schema, fields

class EventSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    time = fields.Str(required=True)
    description = fields.Str()