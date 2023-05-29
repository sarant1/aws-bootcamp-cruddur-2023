from lib.db import db
class AddBioColumnMigration:
  def migrate_sql(self):
    data = """
      ALTER TABLE public.users ADD COLUMN bio text;
    """
    return data
  def rollback_sql(self):
    data = """
      ALTER TABLE public.users DROP COLUMN bio;
    """
    return data
  def migrate(self):
    db.query_commit(self.migrate_sql(),{
    })
  def rollback(self):
    db.query_commit(self.rollback_sql(),{
    })
migration = AddBioColumnMigration()