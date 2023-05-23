from datetime import datetime, timedelta, timezone
from lib.db import db

class CreateReply:
  def run(self, message, cognito_user_id, activity_uuid):
    model = {
      'errors': None,
      'data': None
    }

    if cognito_user_id == None or len(cognito_user_id) < 1:
      model['errors'] = ['cognito_user_id_blank']

    if activity_uuid == None or len(activity_uuid) < 1:
      model['errors'] = ['activity_uuid_blank']

    if message == None or len(message) < 1:
      model['errors'] = ['message_blank'] 
    elif len(message) > 1024:
      model['errors'] = ['message_exceed_max_chars'] 

    if model['errors']:
      # return what we provided
      model['data'] = {
        'message': message,
        'reply_to_activity_uuid': activity_uuid
      }
    else:
      uuid = self.create_reply(cognito_user_id, message, activity_uuid)
      print("uuid <<<<<<<<<<<<<>>>>>>>>>>", uuid, flush=True)
      object_json = self.query_object_activity(uuid)
      model['data'] = object_json
    return model
  
  def create_reply(self, cognito_user_id, message, reply_to_activity_uuid):
      
      print("CREATING REPLY-------------------", flush=True)
      sql = db.template('activities', 'reply')
      return db.query_commit(sql, {
        'cognito_user_id': cognito_user_id,
        'reply_to_activity_uuid': reply_to_activity_uuid,
        'message': message, 
      })
      
  def query_object_activity(self, uuid):
    sql = db.template('activities', 'object')

    db.query_commit(sql)
    #def query_object_activity():
    
    return db.query_object_json(sql, {
      'uuid': uuid,
    })