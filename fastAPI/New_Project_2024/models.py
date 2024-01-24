from sqlalchemy import Column, Integer, String, Float, DateTime, Date,ForeignKey
from sqlalchemy.orm import relationship, Session
from db import Base
from datetime import datetime, date
from fastapi import Depends
from main import get_session

session: Session = Depends(get_session())

class AbstractBaseModel(Base):
    __abstract__ = True
    id = Column(
        Integer,
        primary_key=True,
        index=True,
        name='id',
        autoincrement=True
    )
    created_on = Column(Date, name='createdon',
                        default=datetime.utcnow().date())
    
    @classmethod
    def get_instance(cls, id):
        if id is None:
            raise Exception("ID is mandatory to get instance")
        obj = session.query(cls).filter(cls.id == id)
        if not obj:
            raise Exception("Record not Found")
        return obj

    @classmethod
    def create(cls, schema):
        if not isinstance(schema, dict):
            schema = schema.__dict__
        obj = cls(**schema)
        session.add(obj)
        cls.commit(obj)

    @classmethod
    def commit(cls, obj):
        session.commit(obj)
        session.refresh(obj)

    @classmethod
    def update(cls, id, schema):
        if id is None:
            raise Exception("ID is mandatory to update")
        obj = session.query(cls).filter(cls.id == id)
        if obj:
            obj = obj.update(**schema,synchronize_session=False)
        cls.commit(obj)
        return cls.message("updated")
    
    @classmethod
    def delete(cls, id):
        if id is None:
            raise Exception("ID is mandatory to delete")
        obj = session.query(cls).filter(cls.id == id)
        if obj:
            session.delete(obj)
            cls.commit(obj)
            return cls.message('deleted')

    @classmethod
    def message(cls, msg):
        return f'{msg} successfully.'    

class Company(Base):
    __tablename__ = 'company'

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        name='id',
        autoincrement=True
    )
    name = Column(String(100), 
                  nullable=False)
    employees = relationship('Employee')
    
    def __repr__(self):
        return "<Company(name='%s')>" % (self.name)
    
    @classmethod
    def get_employees(cls, **kwargs):
        q = session.query(cls)
        q = q.join(Employee, cls.id == 
                    Employee.companyId)
        return q
        

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(
            Integer,
            primary_key=True,
            index=True,
            name='id',
            autoincrement=True
        )

    name = Column(String(100), 
                  nullable=False)
    degn = Column(String(100), name='designation',
                  nullable=False)
    doj = Column(Date, name='dateofjoin',
                 nullable=False)
    companyId = Column(Integer, ForeignKey('company.id'))
    company = relationship('Company', foreign_keys=[companyId],
                           back_populates='employees', cascade='delete')
    
    def __repr__(self):
        return "<Employee(name='%s')>" % (self.name)
    

    