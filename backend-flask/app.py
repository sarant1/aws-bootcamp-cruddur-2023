from flask import Flask
from flask import request, g
from flask_cors import cross_origin

from lib.rollbar import init_rollbar
from lib.xray import init_xray
from lib.honeycomb import init_honeycomb
from lib.cors import init_cors
from lib.cognito_jwt_token import jwt_required
from lib.cloudwatch import init_cloudwatch

from services.home_activities import *
from services.notifications_activities import *
from services.user_activities import *
from services.create_activity import *
from services.create_reply import *
from services.search_activities import *
from services.message_groups import *
from services.messages import *
from services.create_message import *
from services.show_activity import *
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from services.users_short import *
from services.update_profile import *


from time import strftime

# provider = TracerProvider()
# processor = BatchSpanProcessor(OTLPSpanExporter())
# provider.add_span_processor(processor)
# trace.set_tracer_provider(provider)
# tracer = trace.get_tracer(__name__)



app = Flask(__name__)

init_cors(app)
## Initialization
init_honeycomb(app)
with app.app_context():
  init_rollbar()
init_xray()

def model_json(model):
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200

@app.route('/api/health-check')
def health_check():
  return {'success': True}, 200

@app.route("/api/message_groups", methods=['GET'])
@jwt_required()
def data_message_groups():
    model = MessageGroups.run(g.cognito_user_id)
    print("MODEL---------------\n", model, flush=True)
    return model_json(model)
  

@app.route("/api/messages/<string:message_group_uuid>", methods=['GET'])
@jwt_required()
def data_messages(message_group_uuid):
    model = Messages.run(
      cognito_user_id=g.cognito_user_id,
      message_group_uuid=message_group_uuid
    )
    return model_json(model)

@app.route("/api/messages", methods=['POST','OPTIONS'])
@cross_origin()
@jwt_required()

def data_create_message():
  message_group_uuid   = request.json.get('message_group_uuid', None)
  user_receiver_handle = request.json.get('handle', None)
  message = request.json['message']

  if message_group_uuid == None:
  # Create for the first time
    model = CreateMessage.run(
    mode="create",
    message=message,
    cognito_user_id=g.cognito_user_id,
    user_receiver_handle=user_receiver_handle
  )
  else:
    # Push onto existing Message Group
    model = CreateMessage.run(
      mode="update",
      message=message,
      message_group_uuid=message_group_uuid,
      cognito_user_id=g.cognito_user_id
    )
  return model_json(model)

@app.route("/api/activities/notifications", methods=['GET'])
def data_notifications():
  data = NotificationsActivites.run()
  return data, 200

def default_home_feed():
  app.logger.debug(e)
  app.logger.debug("unauthenticated")
  data = HomeActivities.run()
  return data, 200

@app.route("/api/activities/home", methods=['GET'])
# @xray_recorder.capture('activities_home')
@jwt_required(on_error=default_home_feed)
def data_home():
  data = HomeActivities.run(cognito_user_id=g.cognito_user_id)
  return data, 200

@app.route("/api/activities/@<string:handle>", methods=['GET'])
#@xray_recorder.capture('activites_users')


#### PASSING samuelarant as handle for now 
def data_handle(handle):
  model = UserActivities.run('samuelarant')
  return model_json(model)

@app.route("/api/activities/search", methods=['GET'])
def data_search():
  term = request.args.get('term')
  model = SearchActivities.run(term)
  return model_json(model)

@app.route("/api/activities", methods=['POST','OPTIONS'])
@cross_origin()
@jwt_required()
def data_activities():
    # user_handle  = 'samuelarant'
    message = request.json['message']
    ttl = request.json['ttl']
    model = CreateActivity.run(message, g.cognito_user_id, ttl) 
    return model_json(model)

@app.route("/api/activities/<string:activity_uuid>", methods=['GET'])
# @xray_recorder.capture('activites_show')
def data_show_activity(activity_uuid):
  data = ShowActivity.run(activity_uuid=activity_uuid)
  return data, 200

@app.route("/api/users/@<string:handle>/short", methods=['GET'])
def data_users_short(handle):
  data = UsersShort.run(handle)
  return data, 200


@app.route("/api/activities/<string:activity_uuid>/reply", methods=['POST','OPTIONS'])
@cross_origin()
def data_activities_reply(activity_uuid):
  user_handle  = 'samuelarant'
  message = request.json['message']
  model = CreateReply.run(message, user_handle, activity_uuid)
  
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200

@app.route("/api/profile/update", methods=['POST','OPTIONS'])
@cross_origin()
@jwt_required()
def data_update_profile():
  bio          = request.json.get('bio',None)
  display_name = request.json.get('display_name',None)
  cognito_user_id = g.cognito_user_id

  model = UpdateProfile.run(
    cognito_user_id=cognito_user_id,
    bio=bio,
    display_name=display_name
  )
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200

if __name__ == "__main__":
  app.run(debug=True)