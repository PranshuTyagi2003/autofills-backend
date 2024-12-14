# Robot Fleet Backend

The **Robot Fleet Backend** is part of a larger project that simulates a fleet of robots, providing their telemetry data through a backend built using **Flask**, **Flask-SocketIO**, and **Flask-CORS**. This backend offers both REST APIs for fetching robot data and real-time WebSocket updates.

## Features

- **Simulated Robot Data**: Simulates robot telemetry data, including:
  - Robot ID (UUID)
  - Online/Offline status (Boolean)
  - Battery Percentage (Integer)
  - CPU Usage (Integer)
  - RAM Consumption (Integer)
  - Last Updated Timestamp
  - Location Coordinates (Latitude, Longitude)
  
- **REST APIs**:
  - `GET /robots`: Retrieves a list of all robots and their status.
  - `GET /robots/<robot_id>`: Retrieves detailed information about a specific robot.
  
- **Real-Time Updates via WebSockets**:
  - The backend sends real-time updates to connected clients (e.g., frontend dashboard) every 5 seconds.
  
- **CORS Support**: Handles cross-origin requests to allow the frontend hosted on a different domain/port to interact with the backend.

## Tools and Technologies

This project uses the following tools and technologies:

- **Flask**: A lightweight web framework for Python to build the web application and APIs.
- **Flask-SocketIO**: Provides WebSocket functionality for real-time communication.
- **Flask-CORS**: Handles Cross-Origin Resource Sharing (CORS) to allow frontend-backend communication across different domains.
- **UUID**: For generating unique robot IDs.
- **Random**: For simulating random telemetry data (battery percentage, CPU usage, etc.).
- **Eventlet**: An asynchronous networking library to handle concurrent WebSocket connections (optional but recommended for production).
- **Python 3.x**: Programming language used to build the backend.
  
### Dependencies

- Flask
- Flask-SocketIO
- Flask-CORS
- Eventlet (optional, for asynchronous handling)
- UUID
- Random

## Installation

### Prerequisites

- Python 3.x (Install from [here](https://www.python.org/downloads/))
- `pip` (Python package installer)

### Steps to Set Up the Project Locally

1. **Clone the Repository**:
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/PranshuTyagi2003/autofills-backend.git
   cd autofills-backend
2. **Create a Virtual Environment (optional but recommended): A virtual environment will help isolate the dependencies:**

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install Dependencies: Install the required Python dependencies using pip:**

pip install -r requirements.txt

4. **Run the Flask App: Start the Flask application:**

python app.py

## Installing Dependencies Manually
pip install Flask flask-socketio flask-cors eventlet
