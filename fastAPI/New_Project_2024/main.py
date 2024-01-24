
from fastapi import FastAPI, Depends, HTTPException
from db import SessionLocal,Base, engine
from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get('/get_company/')
def get_companies(db: Session = Depends(get_session)):
    import pdb;pdb.set_trace()
    from models import Company, Employee
    objs = db.query(Company).all()
    if objs:
        return {"comanies": objs}


@app.get('/{company_id}')
def get_company(company_id: int, db: Session = Depends(get_session)):
    from models import Company, Employee
    obj = Company.get_instance(company_id)
    return {"company": obj.__dict__}
    
