from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

POSTGRES_USER = "admin"
POSTGRES_PASSWORD = "testadmin"
POSTGRES_DB = "xpayback"
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost/{POSTGRES_DB}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
