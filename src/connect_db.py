from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import text
import json



def get_db_configs(json_file):
  with open(json_file, 'r') as f:
      db_config = json.load(f)
  return db_config


def get_engine(user, password, host, port, db):
  url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
  if not database_exists(url):
    create_database(url)
  engine = create_engine(url, pool_size=50, echo=False)
  return engine


def get_engine_from_configs(configs):
   return get_engine(configs["user"], configs["password"], configs["host"], configs["port"], configs["dbname"])


def set_superuser(engine, user):
   with engine.connect() as connection:
    cmd = f"ALTER USER {user} WITH SUPERUSER;"
    connection.execute(text(cmd))
    print(f"Superuser privileges granted to '{user}'.")


db_configs = get_db_configs("db_config.json")
engine = get_engine_from_configs(db_configs)
SessionLocal = sessionmaker(bind=engine)

def get_db():
  session = SessionLocal()
  try:
    yield session
  finally:
    session.close()


# Is used during debug
def init_db():
  set_superuser(engine, db_configs["user"])

if __name__ == '__main__':
   init_db()