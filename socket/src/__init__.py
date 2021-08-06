import os

from flask import Flask
from flask_socketio import SocketIO
from werkzeug.debug import DebuggedApplication

socketio = SocketIO(cors_allowed_origins='*')

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    # this is so we can debug the app, even without running it through flask run
    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    app.config.from_mapping(
        SECRET_KEY='secret',
    )

    # add your routes here! try to write them as blueprints if you can
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import chat

    app.register_blueprint(chat.bp)

    from . import multiplayer

    app.register_blueprint(multiplayer.bp)

    socketio.init_app(app)

    return app