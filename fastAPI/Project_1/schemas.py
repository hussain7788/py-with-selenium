from pydantic import BaseModel

class Employee_Schema(BaseModel):

    id : int
    name : str
    age : int
    designation : str
    salary : float