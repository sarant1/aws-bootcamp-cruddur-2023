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


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'

# SocketIO               
socketio = SocketIO(app, cors_allowed_origins=['*', 'http://localhost:3000'], pingTimeout=60000)

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


@socketio.on('connect')
def connect(argument):
  print("user has connected")

@socketio.on('new message')
def new_message(data):
   print("new message recieved to server")
   print(data, flush=True)

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

if __name__ == "__main__":
  socketio.run(app, debug=True, host='0.0.0.0', port=4567)