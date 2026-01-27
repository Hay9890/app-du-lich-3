from pydantic import BaseModel, EmailStr, Field

class UserRegister(BaseModel):
     username: str = Field(..., min_length=3)
     email: EmailStr
     password: str = Field(..., min_length=6)

class UserInDB(BaseModel):
     username: str
     email: EmailStr
     hashed_password: str
     role: str = "user"

class UserResponse(BaseModel):
     id: str
     username: str
     email: EmailStr