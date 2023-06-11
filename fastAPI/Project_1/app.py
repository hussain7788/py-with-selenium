from fastapi import FastAPI, Depends, HTTPException
from models import Employee
from database import engine, Base, SessionLocal
from schemas import Employee_Schema
from sqlalchemy.orm import Session
from sqlalchemy import select, and_, or_
import logging
from starlette.responses import RedirectResponse
import os
path = os.getcwd()

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

file_name = path + "\\test.log"
logging.basicConfig(filename=file_name, level=logging.INFO)

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get('/get_all_emp/')
def get_all_employees(db: Session = Depends(get_session), emp_name:str= None):

    """
        Fetching all Employees 
    """
    if emp_name:
        data = db.query(Employee).filter(Employee.name==emp_name).all()
    else:
        data = db.query(Employee).all()

    logging.info(f"Successfully fetched all Employees..")
    return data


@app.get('/get_emp/{id}')
def get_employee(id: int, db: Session = Depends(get_session)):

    """
        Fetch Employee data based on Id
    """

    # emp_obj = db.query(Employee).get(id)
    emp_obj = db.get(Employee, id)
    if emp_obj is None:
        raise HTTPException(
            status_code=404,
            detail=f"Employee Id: {id} doesn't exist"
        )
    else:
        logging.info(f"Successfully fetched Employee of Id: {id}")
        return emp_obj

@app.post('/post_emp/')
def post_employee(emp: Employee_Schema, db: Session = Depends(get_session)):

    """
        Adding Employee with validated schema
    """

    emp_obj = Employee(id=emp.id, 
                       name= emp.name, 
                       age= emp.age, 
                       designation= emp.designation, 
                       salary= emp.salary)
    
    db.add(emp_obj)
    db.commit()
    db.refresh(emp_obj)
    logging.info(f"Successfully added Employee..")
    return emp_obj

@app.put('/update_emp/{id}')
def update_employee(id: int, emp: Employee_Schema, db: Session = Depends(get_session)):

    """
        Updating Employee by ID with validation schema
    """

    emp_obj = db.get(Employee, id)

    if emp_obj is None:
        raise HTTPException(
            status_code=404,
            detail=f"Employee Id: {id} doesn't exist"
        )
    else:
        logging.info(f"Successfully fetched Employee by ID: {id}")
        emp_obj.name = emp.name
        emp_obj.age = emp.age
        emp_obj.designation = emp.designation
        emp_obj.salary = emp.salary
        db.commit()
        logging.info(f"Successfully updated Employee data of ID: {id}")
        return emp_obj

@app.delete('/delete_emp/{id}')
def delete_employee(id: int, db: Session = Depends(get_session)):

    """
        Deleting Employee data based on Id
    """
    
    emp_obj = db.get(Employee, id)

    if emp_obj is None:
        raise HTTPException(
            status_code=404,
            detail=f"Employee Id: {id} doesn't exist"
        )
    else:
        db.delete(emp_obj)
        db.commit()
        db.close()
        logging.info(f"Successfully deleted Employee of Id: {id}")
        return f"Employee of Id: {id} was deleted.."