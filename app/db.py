from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# set a database URL
SQLALCHEMY_DATABASE_URL = 'sqlite:///./Library.db'

# create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
    "check_same_thread": False})

# create local session
session_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# create instance for declarative base
Base = declarative_base()
