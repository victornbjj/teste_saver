import jwt
import os 
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from functools import wraps
from flask import request, redirect, url_for


load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")

def generate_token(user_id: int, username: str) -> str:
    payload = {

        "user_id": user_id,
        "username": username,
        "exp" : datetime.now(timezone.utc) + timedelta(hours=2),
        "iat" : datetime.now(timezone.utc)  
    }

    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_token(token: str) -> dict| None:
    try: 
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def jwt_required(f):

    @wraps(f)

    def decorated(*args, **kwargs):
        token = request.cookies.get("access_token_cookie")
        if not token:
            return redirect(url_for("auth.login_page"))

        payload = decode_token(token)
        if payload is None:
            return redirect(url_for("auth.login_page"))


        request.user = payload
        return f(*args, **kwargs)
    return decorated