from flask import Blueprint, request, render_template, redirect, url_for, make_response
from werkzeug.security import check_password_hash
from app.database import get_db_connection
from app.auth.jwt_utils import generate_token

auth_bp = Blueprint("auth", __name__)

COOKIE_NAME = "access_token_cookie" 

@auth_bp.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    conn = get_db_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE username = ?", (username,)
    ).fetchone()
    conn.close()

    if user is None or not check_password_hash(user["password_hash"], password):
        return render_template("login.html", error="Usuário ou senha inválidos")

    token = generate_token(user_id=user["id"], username=user["username"])

    response = make_response(redirect(url_for("agenda.agenda_page")))
    response.set_cookie(
        COOKIE_NAME,
        token,
        httponly=True,       
        samesite="Lax",      
        max_age=2 * 60 * 60  # 2h, bate com a expiração do token
    )
    return response