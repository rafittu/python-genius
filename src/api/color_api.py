from flask_socketio import SocketIO
from flask import Blueprint

color_api_bp = Blueprint('color_api', __name__)
socketio = SocketIO(cors_allowed_origins="*")


def init_sockets(app):
    socketio.init_app(app)


@socketio.on('send_color')
def handle_receive_color(data):
    color = data.get('color')
    timestamp = data.get('timestamp')

    print(f"Received color: {color} at timestamp: {timestamp}")
