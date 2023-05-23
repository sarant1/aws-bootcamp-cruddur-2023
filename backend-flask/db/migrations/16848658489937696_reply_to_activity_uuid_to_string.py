from lib.db import db

class ReplyToActivityUuidToStringMigration:
  def migrate_sql(self):
    data = """
    ALTER TABLE activities DROP COLUMN reply_to_activity_uuid;
    ALTER TABLE activities ADD COLUMN reply_to_activity_uuid uuid;
    """
    return data
  def rollback_sql(self):
    data = """
    ALTER TABLE activities DROP COLUMN reply_to_activity_uuid;
    ALTER TABLE activities ADD COLUMN reply_to_activity_uuid integer;
    """
    return data

  def migrate(self):
    db.query_commit(ReplyToActivityUuidToStringMigration.migrate_sql(self),{
    })

  def rollback(self):
    db.query_commit(ReplyToActivityUuidToStringMigration.rollback_sql(self),{
    })

migration = ReplyToActivityUuidToStringMigration