from app.models import db
from app.models import Tokens
import psycopg2


def query_insert(value):
    try:
        data = Tokens(**value)
        db.session.add(data)
        db.session.commit()

    except Exception as error:
        if isinstance(error.orig, psycopg2.errors.UniqueViolation) is True:
            raise Exception('Duplicate value')

        raise Exception(str(error))

    return True


def query_update(id, value):
    try:
        # get
        token = Tokens.query.get(id)

        # update values
        token.host = value['host']
        token.protocol = value['protocol']
        token.token = value['token']
        token.status = value['status']

        # save
        db.session.commit()

    except Exception as error:
        raise Exception(str(error))

    return True


def query_remove(id):
    try:
        # get
        token = Tokens.query.get(id)
        db.session.delete(token)

        # save
        db.session.commit()

    except Exception as error:
        raise Exception(str(error))

    return True


def query_get(id):
    return Tokens.query.get(id)
