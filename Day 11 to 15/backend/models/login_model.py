# Login model referencing the core User entity in the database
from models.user_model import UserModel

# Export UserModel as UserLoginModel for dedicated authentication contexts
UserLoginModel = UserModel
