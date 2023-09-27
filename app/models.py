from sqlalchemy import Column, ForeignKey, Integer, LargeBinary, String
from sqlalchemy.ext.declarative import declarative_base
from app.db import engine

Base = declarative_base()


class User(Base):
    __tablename__ = "userstwo"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    password = Column(String)


class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True, index=True)
    profile_picture = Column(LargeBinary)
    user_id = Column(Integer, ForeignKey("userstwo.id"))


Base.metadata.create_all(bind=engine)
