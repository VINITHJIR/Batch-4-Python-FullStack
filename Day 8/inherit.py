from pydantic import BaseModel , EmailStr

class UserRegister(BaseModel):
    name:str
    email:EmailStr
    password:str
    phone_no:str

obj1 = UserRegister(name = "Saran" , email ="Saran@gmail.com" , password="1234" , phone_no="9360385470")
print(obj1.email)
