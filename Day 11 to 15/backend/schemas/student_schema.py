from pydantic import BaseModel ,EmailStr

class StudentSchema(BaseModel):
     name: str 
     email:EmailStr 
     phonenumber:int
     department: str
     address: str
     python_mark: int
     java_mark: int
     database_mark: int
