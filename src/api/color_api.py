import re
import logging
from flask_socketio import SocketIO
from flask import Blueprint
from src.database.models.color import Color
from src.database.database import db

color_api_bp = Blueprint('color_api', __name__)
socketio = SocketIO(cors_allowed_origins="*")
logger = logging.getLogger(__name__)

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


def parse_rgb(color_str):
    match = re.match(r'rgb\((\d+),\s*(\d+),\s*(\d+)\)', color_str)
    if match:
        return int(match.group(1)), int(match.group(2)), int(match.group(3))
    raise ValueError("Invalid color format")


def get_color_name(color_str):
    return COLOR_MAP.get(color_str, "unknown")


@socketio.on('send_color')
def handle_receive_color(data):
    color_str = data.get('color')
    timestamp = data.get('timestamp')

    try:
        red, green, blue = parse_rgb(color_str)
        color_name = get_color_name(color_str)
        
        new_color = Color(
            color_name=color_name,
            red=red,
            green=green,
            blue=blue,
            timestamp=timestamp
        )
        db.session.add(new_color)
        db.session.commit()
    except ValueError as e:
        logger.error(f"Error processing color: {e}")
