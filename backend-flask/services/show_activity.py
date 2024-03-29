from datetime import datetime, timedelta, timezone
from lib.db import db

class ShowActivity:
  def run(activity_uuid):
    now = datetime.now(timezone.utc).astimezone()
    
    sql = db.template('activities', 'show')
    results = db.query_array_json(sql, {
      'uuid': activity_uuid,
    })
    print("RESULTS_--------")
    print(results, flush=True)
    return results