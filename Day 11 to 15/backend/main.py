from fastapi import FastAPI
from routes.student_routes import student_router
from core.database import Base, engine
from models.student_details import StudentModel

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(student_router)


@app.get('/abi')
def home():
    return {
        "message":"Hi Guys , Na vanthuten nu sollu"
    }