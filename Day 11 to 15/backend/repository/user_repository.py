from sqlalchemy.orm import Session
from models.user_model import UserModel

# Get user by email to verify uniqueness
def get_user_by_email_repo(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

# Get user by id
def get_user_by_id_repo(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()

# Create user in PostgreSQL database
def create_user_repo(db: Session, user: UserModel):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
