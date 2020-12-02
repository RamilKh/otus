from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.exceptions import BadRequest
from app.models import Tokens, User
from app.quiries.base import query_all
from app.quiries.tokens import (
    query_insert as query_token_insert, query_get as query_token_get,
    query_update as query_token_update, query_remove as query_token_remove,
)
from app.quiries.users import (
    query_insert as query_user_insert, query_get as query_user_get,
    query_update as query_user_update, query_remove as query_user_remove,
)
from app.schemas import SchemaToken, SchemaUser
from marshmallow.exceptions import ValidationError
from werkzeug.security import generate_password_hash


admin_app = Blueprint('admin', __name__)


@admin_app.route('/', endpoint='index')
def admin_index():
    return redirect(url_for('admin.tokens_list'))


"""
######################################################
TOKENS
######################################################
"""


@admin_app.route('/tokens', endpoint='tokens_list')
def admin_tokens_list():
    tokens = query_all(Tokens)
    # render template
    return render_template('tokens/index.html', page='tokens', tokens=tokens)


@admin_app.route('/tokens/add', endpoint='tokens_add', methods=['GET', 'POST'])
def admin_tokens_add():
    if request.method == 'POST':
        form = request.form.to_dict()
        schema = SchemaToken()
        errors = None

        try:
            params = schema.load(form)
            result = query_token_insert(params)
            if result is True:
                return redirect(url_for('admin.tokens_list'))

        except ValidationError as error:
            errors = ''
            for key in error.messages:
                errors += '<p>' + key + ': ' + ', '.join(error.messages[key]) + '</p>'

        except Exception as error:
            errors = error

        # render template
        return render_template('tokens/add.html', page='tokens', form=form, errors=errors)

    else:
        # render template
        return render_template('tokens/add.html', page='tokens')


@admin_app.route('/tokens/edit/<int:id>', endpoint='tokens_edit', methods=['GET', 'POST'])
def admin_tokens_edit(id: int):
    if request.method == 'POST':
        form = request.form.to_dict()
        form['status'] = int(form['status'])
        errors = None

        try:
            schema = SchemaToken()
            params = schema.load(form)
            result = query_token_update(id, params)
            if result is True:
                return redirect(url_for('admin.tokens_edit', id=id))

        except ValidationError as error:
            errors = ''
            for key in error.messages:
                errors += '<p>' + key + ': ' + ', '.join(error.messages[key]) + '</p>'

        except Exception as error:
            errors = error

        # render template
        return render_template('tokens/edit.html', page='tokens', form=form, id=id, errors=errors)

    else:
        form = query_token_get(id)

        if form is None:
            raise BadRequest(f'Token {id} not found')

        form.status = int(form.status)

        # render template
        return render_template('tokens/edit.html', form=form, id=id, page='tokens')


@admin_app.route('/tokens/remove/<int:id>', endpoint='tokens_remove', methods=['POST'])
def admin_tokens_remove(id: int):
    result = query_token_remove(id)
    if result is True:
        return redirect(url_for('admin.tokens_list'))

    # render template
    return render_template('tokens/index.html')


"""
######################################################
USERS
######################################################
"""


@admin_app.route('/users', endpoint='users_list')
def admin_users_list():
    users = query_all(User)
    # render template
    return render_template('users/index.html', page='users', users=users)


@admin_app.route('/users/add', endpoint='users_add', methods=['GET', 'POST'])
def admin_users_add():
    if request.method == 'POST':
        form = request.form.to_dict()
        schema = SchemaUser()
        errors = None

        try:
            params = schema.load(form)
            params['password'] = generate_password_hash(params['password'])

            result = query_user_insert(params)
            if result is True:
                return redirect(url_for('admin.users_list'))

        except ValidationError as error:
            errors = ''
            for key in error.messages:
                errors += '<p>' + key + ': ' + ', '.join(error.messages[key]) + '</p>'

        except Exception as error:
            errors = error

        # render template
        return render_template('users/add.html', page='users', form=form, errors=errors)

    else:
        # render template
        return render_template('users/add.html', page='users')


@admin_app.route('/users/edit/<int:id>', endpoint='users_edit', methods=['GET', 'POST'])
def admin_users_edit(id: int):
    if request.method == 'POST':
        form = request.form.to_dict()
        errors = None

        try:
            # password to secret
            if 'password_new' in form and form['password_new'] is not None and len(form['password_new']) > 1:
                form['password'] = generate_password_hash(form['password_new'])

            # init params
            schema = SchemaUser(only=('name', 'username', 'password'), unknown=True)
            params = schema.load(form)

            # save
            result = query_user_update(id, params)
            if result is True:
                return redirect(url_for('admin.users_edit', id=id))

        except ValidationError as error:
            errors = ''
            for key in error.messages:
                errors += '<p>' + key + ': ' + ', '.join(error.messages[key]) + '</p>'

        except Exception as error:
            errors = error

        # render template
        return render_template('users/edit.html', page='users', form=form, id=id, errors=errors)

    else:
        form = query_user_get(id)

        if form is None:
            raise BadRequest(f'User {id} not found')

        # render template
        return render_template('users/edit.html', form=form, id=id, page='users')


@admin_app.route('/users/remove/<int:id>', endpoint='users_remove', methods=['POST'])
def admin_users_remove(id: int):
    result = query_user_remove(id)
    if result is True:
        return redirect(url_for('admin.users_list'))

    # render template
    return render_template('users/index.html')


"""
######################################################
PAGES
######################################################
"""


@admin_app.route('/<string:name>', endpoint='admin_page')
def admin_page(name):
    # render template
    return render_template('404.html')

