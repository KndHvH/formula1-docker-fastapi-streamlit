import os
import datetime
import jwt
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

class Auth:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return Auth.pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return Auth.pwd_context.hash(password)

    @staticmethod
    def create_access_token(data: dict):
        to_encode = data.copy()
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, os.getenv('SECRET_KEY'), algorithm="HS256")
        return encoded_jwt
