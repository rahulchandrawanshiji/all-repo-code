import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
DEV_DARABASE_URL = os.getenv("DEV_DARABASE_URL")
engine = create_engine(DEV_DARABASE_URL)
sessionlocal = sessionmaker(autocommit=False,autoflush=True,bind=True)
Base = declarative_base
def get_db_session():
    db = sessionlocal()
    try :
        yield db
    finally:
        db.close()
