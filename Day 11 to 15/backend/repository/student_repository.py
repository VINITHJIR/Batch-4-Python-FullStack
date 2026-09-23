from sqlalchemy.orm import Session
from models.student_details import StudentModel
# Create Student
def create_student_repo(db: Session, student: StudentModel):
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


