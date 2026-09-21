from fastapi import APIRouter

student_router = APIRouter()

@student_router.get('/student')
def get_students():
    return {

        "message":"Student get api working"
    }
@student_router.post('/create-student')
def create_student():
    return {

        "message":"Student create api working"
    }
