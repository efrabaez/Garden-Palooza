from flask import Blueprint, send_from_directory

bp = Blueprint("chat", __name__)

@bp.route("/chat/<path:path>")
def chat(path):
	return send_from_directory('static', path)
