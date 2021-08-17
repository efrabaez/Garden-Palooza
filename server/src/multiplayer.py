from flask import Blueprint
from . import socketio
from flask_socketio import emit
from .game.levelGenerator.levelGenerator import GenerateLevel
from src.models import db, GardenModel, UserModel
bp = Blueprint("multiplayer", __name__)

levelInformation = GenerateLevel()

print("Level generated!")

@socketio.on('gameLoaded')
def sendLevel(signal):
    if signal == 'ok':
        print("sending level to client")
        return levelInformation

def messageReceived(methods=['GET', 'POST']):
    print('we got a message!')

@socketio.on('event')
def handle_event(json, methods=['GET', 'POST']):
    print('received an event: '+ str(json))
    socketio.emit('response', json, callback=messageReceived)
