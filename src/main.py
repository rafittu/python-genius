from flask import Flask
from api.color_api import color_api_bp, init_sockets, socketio


def create_app():
    app = Flask(__name__)

    app.register_blueprint(color_api_bp)

    init_sockets(app)

    return app


def main():
    print("🎨 Genius!")

    app = create_app()
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)


if __name__ == "__main__":
    main()
