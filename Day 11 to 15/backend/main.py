from fastapi import FastAPI
from routes.student_routes import student_router
from core.database import Base, engine
from models.student_details import StudentModel

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
Base.metadata.create_all(bind=engine)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student_router)


@app.get('/abi')
def home():
    return {
        "message":"Hi Guys , Na vanthuten nu sollu"
    }