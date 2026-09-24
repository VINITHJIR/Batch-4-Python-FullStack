from sqlalchemy.orm import Session
from models.student_details import StudentModel
# Create Student
def create_student_repo(db: Session, student: StudentModel):
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

# Get All Students
def get_all_students_repo(db: Session):
    return db.query(StudentModel).all()

# Get Student By ID
def get_student_by_id_repo(db: Session, student_id: int):
    return db.query(StudentModel).filter(StudentModel.id == student_id).first()

# Update Student
def update_student_repo(db: Session, student: StudentModel):
    db.commit()
    db.refresh(student)
    return student

# Delete Student
def delete_student_repo(db: Session, student: StudentModel):
    db.delete(student)
    db.commit()
    return student



