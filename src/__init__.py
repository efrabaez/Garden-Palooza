import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='secret',
    )

    # add your routes here! try to write them as blueprints if you can
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app