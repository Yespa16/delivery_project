from connect_db import engine
from sqlalchemy import asc, desc, func, text


def column_exists(table, column):
  with engine.connect() as connection:
    result = connection.execute(
                  text(f"""
                      SELECT column_name
                      FROM information_schema.columns
                      WHERE table_name = '{table}' AND column_name = '{column}';
                  """)
              ).fetchone()
    return True if result else False
  

def index_exists(table, index):
  with engine.connect() as connection:
    with connection.begin() as transaction:
      # Check if the index exists
      result = connection.execute(
          text(f"""
              SELECT indexname
              FROM pg_indexes
              WHERE tablename = '{table}' AND indexname = '{index}';
          """)
      ).fetchone()
      return True if result else False