from flask import Blueprint, jsonify, make_response, request
from app.classes import Peer

api_app = Blueprint('api', __name__, url_prefix='/api')


@api_app.route('/list', methods=['GET'])
def list_view():
    peer = Peer()
    result = peer.get_all()

    data = dict()
    if result['returncode'] == 0:
        data['result'] = True
        data['data'] = result['data']

        return make_response(jsonify(data), 200)

    else:
        data['result'] = False
        data['data'] = result['data']
        return make_response(jsonify(data), 400)


@api_app.route('/get/<int:port>', methods=['GET'])
def get_view(port):
    peer = Peer()
    result = peer.get(port)

    data = dict()

    if result['returncode'] == 0:
        data['result'] = True
        data['data'] = result['data']

        return make_response(jsonify(data), 200)

    else:
        data['result'] = False
        return make_response(jsonify(data), 400)


@api_app.route('/start', methods=['POST'])
def start_view():
    data = dict()

    # get and check params
    params = request.get_json()
    port = params.get('port', None)
    if port is None:
        data['result'] = False
        data['message'] = 'Pass parameters'
        return make_response(jsonify(data), 400)

    # start docker container
    peer = Peer()
    result = peer.start(port)

    if result['returncode'] == 0:
        data['result'] = True
        data['container'] = result['data']
        data['port'] = port

        return make_response(jsonify(data), 200)

    else:
        data['result'] = False
        data['message'] = "Container haven't run"
        return make_response(jsonify(data), 400)


@api_app.route('/stop/<int:port>', methods=['GET'])
def stop_view(port):
    peer = Peer()
    result = peer.stop(port=port)

    data = dict()

    if result['returncode'] == 0:
        data['result'] = True
        data['container'] = result['data']
        data['port'] = port

        return make_response(jsonify(data), 200)

    else:
        data['result'] = False
        data['message'] = 'Container not found'

        return make_response(jsonify(data), 400)


@api_app.route('/remove/<int:port>', methods=['GET'])
def remove_view(port):
    peer = Peer()
    result = peer.remove(port=port)

    data = dict()

    if result['returncode'] == 0:
        data['result'] = True
        data['container'] = result['data']
        data['port'] = port

        return make_response(jsonify(data), 200)

    else:
        data['result'] = False
        data['message'] = 'Container not found or not stopped'

        return make_response(jsonify(data), 400)


@api_app.route('/clear/<int:port>', methods=['GET'])
def clear_view(port):
    peer = Peer()
    result = peer.clear(port=port)
    stop, remove = result

    # format result
    data = dict()
    if stop['returncode'] == 0 and remove['returncode'] == 0:
        data['result'] = True
        data['port'] = port

        return make_response(jsonify(data), 200)

    else:
        data['result'] = False
        data['message'] = 'Container not found'
        return make_response(jsonify(data), 400)
