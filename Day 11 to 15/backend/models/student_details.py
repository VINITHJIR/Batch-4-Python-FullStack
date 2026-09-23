from sqlalchemy import Column, Integer, String, Float , TIMESTAMP,func
from core.database import Base
class StudentModel(Base):
  __tablename__ = "students"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  email  = Column(String)
  phonenumber = Column(String)
  department = Column(String)
  address = Column(String)
  python_mark = Column(Integer)
  java_mark = Column(Integer)
  database_mark = Column(Integer)
  percentage = Column(Float)
  created_at = Column(TIMESTAMP, server_default=func.now())
  updated_at = Column(TIMESTAMP, onupdate=func.now())
