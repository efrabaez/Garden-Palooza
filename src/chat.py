from flask import Blueprint, send_from_directory
from . import socketio
from flask_socketio import emit

bp = Blueprint("chat", __name__)

@bp.route("/chat/<path:path>")
def chat(path):
	return send_from_directory('static', path)

def messageReceived(methods=['GET', 'POST']):
    print('we got a message!')

@socketio.on('event')
def handle_event(json, methods=['GET', 'POST']):
    print('received an event: '+ str(json))
    socketio.emit('response', json, callback=messageReceived)
