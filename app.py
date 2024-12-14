from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit # type: ignore
from flask_cors import CORS
import random
import time
import threading
import uuid
from datetime import datetime

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Initial fake robot data
robots = []

# Generate mock robot data
def generate_robot_data():
    global robots
    robots = [
        {
            "Robot ID": str(uuid.uuid4()),
            "Online/Offline": bool(random.getrandbits(1)),
            "Battery Percentage": random.randint(1, 100),
            "CPU Usage": random.randint(0, 100),
            "RAM Consumption": random.randint(1000, 8000),
            "Last Updated": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "Location Coordinates": [
                round(random.uniform(-90, 90), 6),
                round(random.uniform(-180, 180), 6)
            ]
        } for _ in range(100)
    ]

def update_robot_data():
    while True:
        time.sleep(5)
        for robot in robots:
            robot["Online/Offline"] = bool(random.getrandbits(1))
            robot["Battery Percentage"] = max(0, robot["Battery Percentage"] - random.randint(0, 5))
            robot["CPU Usage"] = random.randint(0, 100)
            robot["RAM Consumption"] = random.randint(1000, 8000)
            robot["Last Updated"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            robot["Location Coordinates"] = [
                round(random.uniform(-90, 90), 6),
                round(random.uniform(-180, 180), 6)
            ]
        socketio.emit('robot_data_update', robots)

@app.route('/robots', methods=['GET'])
def get_robots():
    """Endpoint to get the list of robots."""
    return jsonify(robots)

@app.route('/robots/<robot_id>', methods=['GET'])
def get_robot(robot_id):
    """Endpoint to get details of a single robot by ID."""
    robot = next((robot for robot in robots if robot["Robot ID"] == robot_id), None)
    if robot:
        return jsonify(robot)
    return jsonify({"error": "Robot not found"}), 404

@socketio.on('connect')
def handle_connect():
    emit('robot_data_update', robots)

if __name__ == '__main__':
    # Generate initial robot data
    generate_robot_data()

    # Start the background thread for updating data
    threading.Thread(target=update_robot_data, daemon=True).start()

    # Run the Flask app with WebSocket support
    socketio.run(app, host='0.0.0.0', port=5000)
