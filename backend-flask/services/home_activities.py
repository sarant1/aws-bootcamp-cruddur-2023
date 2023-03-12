from datetime import datetime, timedelta, timezone
from opentelemetry import trace
import logging
from lib.db import pool

tracer = trace.get_tracer("home.activites")

class HomeActivities:
  def run(cognito_user_id=None):
    #logger.info("HomeActivities")
    with tracer.start_as_current_span("run-home-activites-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())

      sql = """
      SELECT * FROM activities
      """
      json = {}
      with pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(sql)
          # this will return a tuple
          # the first field being the data
          json = cur.fetchall()
          print("=3-----==")
          print(json)
          for record in cur:
            print(Record)
      return json[0]
      return results