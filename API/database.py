from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pyodbc

username = "SA"
password = "W@nclouds123"
server = "ehsan-wancloud,1433"
database = "lost_items"
SQLALCHEMY_DATABASE_URL='mssql+pyodbc://'+username+':'+password+'@' + server + '/' + database + '?driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
