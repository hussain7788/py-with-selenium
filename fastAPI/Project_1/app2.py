from fastapi import FastAPI, Depends, HTTPException
from models import Employee, Student
from database2 import engine, base,session

base.metadata.create_all(bind=engine)
app2 = FastAPI()



@app2.get("/")
def main():
    return "hello"