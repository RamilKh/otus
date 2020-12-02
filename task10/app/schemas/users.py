from marshmallow import Schema, fields


class SchemaUser(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    name = fields.String(required=True)
    password = fields.String(required=False)
