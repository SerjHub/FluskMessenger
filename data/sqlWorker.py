from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import *

# PATH = "mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>"
# engine = create_engine(PATH, pool_recycle=3600)
#
# Base = declarative_base()
#
# USERS_TABLE = 'all_users_table'
#
# def get_user_table():
#     connection = engine.connect()
#     metadata = db.MetaData()
#     users = db.Table(USERS_TABLE, metadata, autoload=True, autoload_with=engine)
#     print(users.columns.key())
#
# class Users(Base):
#     __tablename__ = USERS_TABLE
#     fullLogin = Column(String, primary_key=True)
#     login = Column(String)
#     password = Column(String)
#     uniqueId = Column(String)
#     about = Column(String)
#
#
# Users.__table__.create(bind=engine, checkfirst=True)
