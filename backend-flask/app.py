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

# Routes
import routes.activities
import routes.general
import routes.users
import routes.messages

from time import strftime

app = Flask(__name__)

init_cors(app)
## Initialization
init_honeycomb(app)
with app.app_context():
  init_rollbar(app)
init_xray(app)

# ----- load routes -----
routes.activities.load(app)
routes.general.load(app)
routes.users.load(app)
routes.messages.load(app)


if __name__ == "__main__":
  app.run(debug=True)