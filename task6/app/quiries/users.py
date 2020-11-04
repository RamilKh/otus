from app.models import db
from app.models import User
import psycopg2


def query_get(id):
    return User.query.get(id)


def query_authentication(username):
    return User.query.filter_by(username=username).first()


def query_insert(value):
    try:
        data = User(**value)
        db.session.add(data)
        db.session.commit()

    except Exception as error:
        print(error)
        if isinstance(error.orig, psycopg2.errors.UniqueViolation) is True:
            raise Exception('Duplicate value')

        raise Exception(str(error))

    return True


def query_update(id, value):
    try:
        # get
        user = User.query.get(id)

        # update values
        user.username = value['username']
        user.name = value['name']
        if 'password' in value and value['password'] is not None:
            user.password = value['password']

        # save
        db.session.commit()

    except Exception as error:
        raise Exception(str(error))

    return True


def query_remove(id):
    try:
        # get
        token = User.query.get(id)
        db.session.delete(token)

        # save
        db.session.commit()

    except Exception as error:
        raise Exception(str(error))

    return True
