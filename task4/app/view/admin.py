from flask import Blueprint, render_template, redirect, url_for
from app.classes import Peer
from werkzeug.exceptions import BadRequest

admin_app = Blueprint('admin', __name__, url_prefix='/admin')


@admin_app.route('/', endpoint='index')
def admin_index():
    return redirect(url_for('admin.containers_list'))


"""
######################################################
CONTAINERS
######################################################
"""


@admin_app.route('/containers', endpoint='containers_list')
def admin_containers_list():
    peer = Peer()

    # get all docker containers
    data = peer.get_all()
    containers = data['data']

    # render template
    return render_template('containers/index.html', page='containers', containers=containers)


@admin_app.route('/containers/<string:id>', endpoint='containers_item')
def admin_containers_item(id: str):
    peer = Peer()

    # get docker container by id
    data_container = peer.get_by_id(id)
    container = None
    if len(data_container['data']) > 0:
        container = data_container['data'][0]
    else:
        raise BadRequest(f'Container {id} not found')

    # render template
    return render_template('containers/item.html', page='containers', id=id, container=container)


@admin_app.route('/containers/<string:id>/start', endpoint='containers_start')
def containers_start(id: str):
    peer = Peer()
    result = dict()

    # get docker container by id
    data_container = peer.get_by_id(id)
    container = None
    if len(data_container['data']) > 0:
        container = data_container['data'][0]

        # stop docker container
        data_result = peer.start_by_id(id=container['id'])

        result['code'] = data_result['returncode']
        if data_result['returncode'] == 0:
            return redirect(url_for('admin.containers_item', id=container['id']))
        else:
            # get docker container by id
            data_container = peer.get_by_id(id)
            if len(data_container['data']) > 0:
                container = data_container['data'][0]

            result['message'] = f"Something happend by starting. The returncode is {result['code']}"
    else:
        raise BadRequest(f'Container {id} not found')

    # render template
    return render_template('containers/item.html', page='containers', id=id, container=container, result=result)


@admin_app.route('/containers/<string:id>/stop', endpoint='containers_stop')
def containers_stop(id: str):
    peer = Peer()
    result = dict()

    # get docker container by id
    data_container = peer.get_by_id(id)
    container = None
    if len(data_container['data']) > 0:
        container = data_container['data'][0]

        # stop docker container
        data_result = peer.stop_by_id(id=container['id'])

        result['code'] = data_result['returncode']
        if data_result['returncode'] == 0:
            return redirect(url_for('admin.containers_item', id=container['id']))
        else:
            # get docker container by id
            data_container = peer.get_by_id(id)

            if len(data_container['data']) > 0:
                container = data_container['data'][0]

            result['message'] = f"Something happend by stopping. The returncode is {result['code']}"
    else:
        raise BadRequest(f'Container {id} not found')

    # render template
    return render_template('containers/item.html', page='containers', id=id, container=container, result=result)


@admin_app.route('/containers/<string:id>/clear', endpoint='containers_clear')
def containers_clear(id: str):
    peer = Peer()
    result = dict()

    # get docker container by id
    data_container = peer.get_by_id(id)
    container = None
    if len(data_container['data']) > 0:
        container = data_container['data'][0]

        # stop docker container
        data_result, _ = peer.clear_by_id(id=container['id'])

        result['code'] = data_result['returncode']
        if data_result['returncode'] == 0:
            return redirect(url_for('admin.containers_list'))
        else:
            # get docker container by id
            data_container = peer.get_by_id(id)

            if len(data_container['data']) > 0:
                container = data_container['data'][0]

            result['message'] = f"Something happend by clearing. The returncode is {result['code']}"
    else:
        raise BadRequest(f'Container {id} not found')

    # render template
    return render_template('containers/item.html', page='containers', id=id, container=container, result=result)


"""
######################################################
PAGES
######################################################
"""


@admin_app.route('/about', endpoint='about_page')
def about_page():
    # render template
    return render_template('about/index.html', page='about')


@admin_app.route('/<string:name>', endpoint='admin_page')
def admin_page(name):
    # render template
    return render_template('404.html')

