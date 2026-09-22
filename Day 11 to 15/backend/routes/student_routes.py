from fastapi import APIRouter
from schemas.student_schema import StudentSchema
from service.student_service import calculate_percentage
student_router = APIRouter()


@student_router.post('/create-student')
def create_student(snsstudent:StudentSchema):

    percentage = calculate_percentage(snsstudent)
    print(percentage)
    return {
        "message": "Student create api working",
        "name":snsstudent.name,
        "email":snsstudent.email,
        "phonenumber":snsstudent.phonenumber,
        "department":snsstudent.department,
        "python_mark":snsstudent.python_mark,
        "java_mark":snsstudent.java_mark,
        "database_mark":snsstudent.database_mark,
        "address":snsstudent.address,
        "Final Percentage":percentage
    }
   
