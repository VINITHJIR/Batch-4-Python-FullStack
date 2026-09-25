from fastapi import FastAPI
from routes.student_routes import student_router
from routes.user_register_routes import user_router
from routes.user_login_routes import login_router
from core.database import Base, engine
from models.student_details import StudentModel
from models.user_model import UserModel

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Batch 4 Full Stack System")
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
app.include_router(user_router)
app.include_router(login_router)


@app.get('/abi')
def home():
    return {
        "message":"Hi Guys , Na vanthuten nu sollu"
    }