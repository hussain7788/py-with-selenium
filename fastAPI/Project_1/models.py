from sqlalchemy import Column, Integer, String, Float, DateTime, Date
from database import Base

class Employee(Base):

    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    designation = Column(String(50))
    salary = Column(Float)

class Student(Base):

    __tablename__ = 'student'

    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    course = Column(String(50))
    