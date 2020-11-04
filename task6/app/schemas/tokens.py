from marshmallow import Schema, fields


class SchemaToken(Schema):
    id = fields.Integer(dump_only=True)
    host = fields.String(required=True)
    protocol = fields.String(required=True)
    token = fields.String(required=True)
    status = fields.Integer(required=True)
