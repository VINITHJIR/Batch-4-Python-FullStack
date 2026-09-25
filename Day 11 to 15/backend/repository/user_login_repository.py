from sqlalchemy.orm import Session
from models.user_model import UserModel

# Lookup user by email for authentication
def find_user_by_email_repo(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

# Lookup user by primary key id
def find_user_by_id_repo(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()
