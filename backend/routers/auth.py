from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from database.queries import AuthQueries
from auth.auth import Auth

from fastapi import APIRouter
from auth.models import User

router = APIRouter()


@router.post("/register")
async def register(user: User):
    if AuthQueries.get_user_and_hash_by_username(username=user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    
    AuthQueries.create_user(user)
    return {"message": "User registered successfully"}


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm):
    user = AuthQueries.get_user_and_hash_by_username(username=form_data.username)
    if not user or not Auth.verify_password(form_data.password, user.hash):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = Auth.create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}