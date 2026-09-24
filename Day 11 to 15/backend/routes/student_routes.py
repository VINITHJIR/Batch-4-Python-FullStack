from fastapi import APIRouter, Depends, HTTPException, status
from schemas.student_schema import StudentSchema
from service.student_service import calculate_percentage
from repository.student_repository import (
    create_student_repo,
    get_all_students_repo,
    get_student_by_id_repo,
    update_student_repo,
    delete_student_repo
)
from core.database import get_db
from models.student_details import StudentModel
from sqlalchemy.orm import Session

student_router = APIRouter()


# 1. Create Student
@student_router.post('/create-student')
def create_student(snsstudent: StudentSchema, db: Session = Depends(get_db)):

    percentage = calculate_percentage(snsstudent)
    student_model = StudentModel(
        name=snsstudent.name,
        email=snsstudent.email,
        phonenumber=snsstudent.phonenumber,
        department=snsstudent.department,
        python_mark=snsstudent.python_mark,
        java_mark=snsstudent.java_mark,
        database_mark=snsstudent.database_mark,
        address=snsstudent.address,
        percentage=percentage
    )

    created_student = create_student_repo(db=db, student=student_model)
    
    return {
        "message": "Student create api working",
        "id": created_student.id,
        "name": created_student.name,
        "email": created_student.email,
        "phonenumber": created_student.phonenumber,
        "department": created_student.department,
        "python_mark": created_student.python_mark,
        "java_mark": created_student.java_mark,
        "database_mark": created_student.database_mark,
        "created_at": created_student.created_at,
        "address": created_student.address,
        "Final Percentage": created_student.percentage
    }


# 2. Get All Students
@student_router.get('/get-all-students')
@student_router.get('/students')
def get_all_students(db: Session = Depends(get_db)):
    students = get_all_students_repo(db=db)
    return {
        "message": "Students fetched successfully",
        "total": len(students),
        "data": students
    }


# 3. Get Student By ID
@student_router.get('/get-student/{student_id}')
@student_router.get('/students/{student_id}')
def get_student_by_id(student_id: int, db: Session = Depends(get_db)):
    student = get_student_by_id_repo(db=db, student_id=student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {student_id} not found"
        )
    return {
        "message": "Student fetched successfully",
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "phonenumber": student.phonenumber,
        "department": student.department,
        "python_mark": student.python_mark,
        "java_mark": student.java_mark,
        "database_mark": student.database_mark,
        "created_at": student.created_at,
        "address": student.address,
        "Final Percentage": student.percentage
    }


# 4. Update Student
@student_router.put('/update-student/{student_id}')
@student_router.put('/students/{student_id}')
def update_student(student_id: int, snsstudent: StudentSchema, db: Session = Depends(get_db)):
    student = get_student_by_id_repo(db=db, student_id=student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {student_id} not found"
        )

    percentage = calculate_percentage(snsstudent)

    student.name = snsstudent.name
    student.email = snsstudent.email
    student.phonenumber = snsstudent.phonenumber
    student.department = snsstudent.department
    student.python_mark = snsstudent.python_mark
    student.java_mark = snsstudent.java_mark
    student.database_mark = snsstudent.database_mark
    student.address = snsstudent.address
    student.percentage = percentage

    updated_student = update_student_repo(db=db, student=student)

    return {
        "message": "Student updated successfully",
        "id": updated_student.id,
        "name": updated_student.name,
        "email": updated_student.email,
        "phonenumber": updated_student.phonenumber,
        "department": updated_student.department,
        "python_mark": updated_student.python_mark,
        "java_mark": updated_student.java_mark,
        "database_mark": updated_student.database_mark,
        "created_at": updated_student.created_at,
        "address": updated_student.address,
        "Final Percentage": updated_student.percentage
    }


# 5. Delete Student
@student_router.delete('/delete-student/{student_id}')
@student_router.delete('/students/{student_id}')
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = get_student_by_id_repo(db=db, student_id=student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {student_id} not found"
        )

    delete_student_repo(db=db, student=student)

    return {
        "message": "Student deleted successfully",
        "id": student_id
    }

   
