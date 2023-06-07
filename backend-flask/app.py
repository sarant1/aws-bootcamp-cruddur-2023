from flask import Flask
from flask import request, g
from flask_cors import cross_origin

from lib.rollbar import init_rollbar
from lib.xray import init_xray
from lib.honeycomb import init_honeycomb
from lib.cors import init_cors
from lib.cognito_jwt_token import jwt_required
from lib.cloudwatch import init_cloudwatch
from lib.helpers import model_json

import os

# Routes
import routes.activities
import routes.general
import routes.users
import routes.messages

from time import strftime

from flask_socketio import SocketIO
from flask_socketio import join_room, leave_room

import random
import string


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'

# SocketIO
frontend = os.getenv('FRONTEND_URL')
backend = os.getenv('BACKEND_URL')
origins = [frontend, backend]
             
socketio = SocketIO(app, cors_allowed_origins=origins, pingTimeout=60000)

init_cors(app)


## Initialization
# init_honeycomb(app)
# with app.app_context():
#   init_rollbar(app)
# init_xray(app)

# ----- load routes -----
routes.activities.load(app)
routes.general.load(app)
routes.users.load(app)
routes.messages.load(app)


def generate_random_string(length):
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return random_string


@socketio.on('connect')
def connect(argument):
  print("user has connected")

@socketio.on('new message')
def new_message(data):

    recieved_message = {
        'display_name': data['display_name'],
        'message': data['message'],
        'handle': data['handle'],
        'key': generate_random_string(10),
        'created_at': 'now'
    }
    socketio.emit('new message', recieved_message, to=data['room'], include_self=False)

# Joining a room
@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    print(f"User {username} has joined room {room}", flush=True)
    socketio.send(username + ' has entered the room.', to=room)

# Leaving a room
@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    socketio.send(username + ' has left the room.', to=room)

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

if __name__ == "__main__":
  socketio.run(app, debug=True, host='0.0.0.0', port=4567)