from fastapi import FastAPI, Depends, HTTPException
from models import Employee, Student
from database2 import engine, base, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import select, and_, or_

base.metadata.create_all(bind=engine)
app2 = FastAPI()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


# @app2.get('/')
# def get_all_students(db: Session = Depends(get_session)):

#     data = db.query(Student).all()
#     return data




@app2.get('/add/')
def add():

    std1 = Student(name='hussain', age=25, course='MPC')
    std2 = Student(name='valli', age=26, course='BIPC')
    std3 = Student(name='anil', age=27, course='CEC')
    std4 = Student(name='sunil', age=28, course='MEC')


    with SessionLocal() as se:
        se.add_all([std1,std2,std3, std4])
        se.commit()

    return 'added'

@app2.get('/get_all/')
def get_students():

    objs = []
    with SessionLocal() as se:
        stm = select(Student)
        objs = se.scalars(stm).all()


    return objs

@app2.delete('/')
def delete_students():

    with SessionLocal() as se:
        stm = select(Student)
        objs = se.scalars(stm).all()
        
        for obj in objs:
            se.delete(obj)
            se.commit()

    return 'deleted'

@app2.get('/')
def test(db: Session = Depends(get_session)):
    # qr = db.query(Student).all()
    # qr = db.query(Student.name, Student.course).filter(Student.name.in_(['hussain','valli']))
    # qr = db.query(Student).filter(and_(Student.age >= 27, Student.age <=30)).all()
    # qr = db.query(Student).filter(or_(Student.age >= 27, Student.age <=30)).all()
    # qr = db.query(Student).filter(Student.age.between(27,30)).all()
    qr = db.query(Student).filter(Student.age.between(27,30)).all()
    qr = db.query(Student)
    qr.filter(Student.age.notin_([26,28])).all()
    qr.filter(Student.name.like('%hu%'))
    qr.filter(Student.name.notlike('%hu%')).all()
    qr.filter(Student.name.is_(None))
    qr.filter(Student.name.isnot(None))
    qr.filter(Student.name.startswith('h')).all()
    qr.filter(Student.name.endswith('l')).all()
    qr.filter(Student.name.contains('il')).all()
    

### Joins
    se.query(Company).join(Employee).all()
    se.query(Company).join(Employee).filter(and_(Company.name=='google',Employee.age>=26)).one().employees
    se.query(Company).outerjoin(Employee).all() # left outer join

### textual SQL
    from sqlalchemy import text

    se.query(Company).filter(text("id>=2")).all()
    se.query(Company).filter(text("id>=2")).order_by(text('id')).all()
    se.query(Company).filter(text("id>=:value and name=:name")).params(value=2, name='infosys').all()

### func

    from sqlalchemy import func

    se.query(Company.name, func.count(Company.name)).group_by(Company.name).all()
    se.query(Company.name, func.count(Employee.name)).join(Employee).group_by(Company.name).all() # count
    se.query(func.max(Employee.salary)).select_from(Employee).all()  # max
    se.query(func.min(Employee.salary)).select_from(Employee).all() # min
    se.query(func.sum(Employee.salary)).select_from(Employee).all() # sum

## union, union_all

    se.query(Company).union(se.query(Employee)).all()
    se.query(Company).union_all(se.query(Employee)).all()

    return qr

