from flask import Blueprint, redirect, url_for

pages_app = Blueprint('pages', __name__, url_prefix='/')


@pages_app.route('/', endpoint='index')
def index():
    return redirect(url_for('admin.tokens_list'))
