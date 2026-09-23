from fastapi import APIRouter , Depends
from schemas.student_schema import StudentSchema
from service.student_service import calculate_percentage
from repository.student_repository import create_student_repo
from core.database import get_db
from models.student_details import StudentModel
from sqlalchemy.orm import Session
student_router = APIRouter()


@student_router.post('/create-student')
def create_student( snsstudent:StudentSchema, db: Session = Depends(get_db)):

    percentage = calculate_percentage(snsstudent)
    student_model  = StudentModel(
        name = snsstudent.name,
        email = snsstudent.email,
        phonenumber = snsstudent.phonenumber,
        department = snsstudent.department,
        python_mark = snsstudent.python_mark,
        java_mark = snsstudent.java_mark,
        database_mark = snsstudent.database_mark,
        address = snsstudent.address,
        percentage = percentage
    )

    created_student = create_student_repo(db=db,student=student_model)
    
    return {
        "message": "Student create api working",
        "id":created_student.id,
        "name":created_student.name,
        "email":created_student.email,
        "phonenumber":created_student.phonenumber,
        "department":created_student.department,
        "python_mark":created_student.python_mark,
        "java_mark":created_student.java_mark,
        "database_mark":created_student.database_mark,
        "created_at":created_student.created_at,
        "address":created_student.address,
        "Final Percentage":created_student.percentage
    }
   
