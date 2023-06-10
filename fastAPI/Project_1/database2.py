from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Employee, Student
from datetime import date


engine = create_engine('sqlite:///student.db')

base = declarative_base()

session = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)




