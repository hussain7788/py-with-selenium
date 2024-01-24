from sqlalchemy import Column, Integer, String, Float, DateTime, Date,ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from database2 import base
from datetime import datetime

class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

    employees = relationship('Employee', back_populates='company')

    def __repr__(self):
        return "<Company(name='%s')>" % (self.name)


class Employee(Base):

    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    designation = Column(String(50))
    salary = Column(Float)

    company_id = Column(Integer, ForeignKey('company.id'))

    company = relationship('Company', back_populates='employees', cascade='all')

    def __repr__(self):
        return "<Employee(name='%s')>" % (self.name)

class Student(base):

    __tablename__ = 'student'

    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    course = Column(String(50))
    doj = Column(Date, default=datetime.utcnow)
    
    def __repr__(self):
        return "<Student(name='%s')>" % (self.name)