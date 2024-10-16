from flask_socketio import SocketIO
from flask import Blueprint

color_api_bp = Blueprint('color_api', __name__)
socketio = SocketIO(cors_allowed_origins="*")

COLOR_MAP = {
    "rgb(0, 0, 255)": "blue",
    "rgb(0, 255, 255)": "blue-green",
    "rgb(0, 255, 0)": "green",
    "rgb(128, 255, 0)": "yellow-green",
    "rgb(255, 255, 0)": "yellow",
    "rgb(255, 192, 0)": "yellow-orange",
    "rgb(255, 128, 0)": "orange",
    "rgb(255, 64, 0)": "red-orange",
    "rgb(255, 0, 0)": "red"
}


def init_sockets(app):
    socketio.init_app(app)


@socketio.on('send_color')
def handle_receive_color(data):
    color = data.get('color')
    timestamp = data.get('timestamp')

    print(f"Received color: {color} at timestamp: {timestamp}")
