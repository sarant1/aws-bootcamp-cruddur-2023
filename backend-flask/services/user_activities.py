from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder
from lib.db import db

class UserActivities:
  def run(user_handle):
    try:
      # x-ray -----
      segment = xray_recorder.begin_segment('user_activities')
      model = {
        'errors': None,
        'data': None
      }

      #x-rayy
      #now = datetime.now(timezone.utc).astimezone()
      
    
      if user_handle == None or len(user_handle) < 1:
        model['errors'] = ['blank_user_handle']
      else:
        sql = db.template('activities', 'home')
        results = db.query_object_json(sql)
        model['data'] = results
      

      subsegment = xray_recorder.begin_subsegment('mock-data')
      # x-ray ----

      now = datetime.now(timezone.utc).astimezone()
      dict = {
         "now": now.isoformat(),
         "results-size": len(model['data'])
       }
      subsegment.put_metadata('key', dict, 'namespace')

    finally:
      # close the subsegment
      # xray_recorder.end_subsegment()
      return model