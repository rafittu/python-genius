import re
import logging
from flask_socketio import SocketIO
from flask import Blueprint
from database.models.color import Color
from database.database import db
from models.lstm_color_predictor import train_model, predict_next_color

color_api_bp = Blueprint('color_api', __name__)
socketio = SocketIO(cors_allowed_origins="*")
logger = logging.getLogger(__name__)

color_buffer = []

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


def map_rgb_to_color_name(rgb_value):
    closest_color = min(COLOR_MAP.keys(), key=lambda x: sum(abs(int(c) - v) for c, v in zip(x[4:-1].split(', '), rgb_value)))
    return COLOR_MAP[closest_color]

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

        color_buffer.append(new_color)

        print(f"Buffer len: {len(color_buffer)}")

        if len(color_buffer) == 9:
            predicted_rgb = predict_next_color()
            predicted_color_name = map_rgb_to_color_name(predicted_rgb)

            logger.info(f"Predicted next color (RGB): {predicted_color_name} {predicted_rgb}")
            print(f"Predicted next color (RGB): {predicted_color_name} {predicted_rgb}")

            train_model(n=10)

            color_buffer.clear()

        if len(color_buffer) == 10:
            color_buffer.clear()

    except ValueError as e:
        logger.error(f"Error processing color: {e}")
