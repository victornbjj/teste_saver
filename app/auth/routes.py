import sqlite3
import logging

from flask import Blueprint, request, render_template, redirect, url_for, make_response
from werkzeug.security import check_password_hash
from app.database import get_db_connection
from app.auth.jwt_utils import generate_token


logger = logging.getLogger(__name__)

auth_bp = Blueprint("auth", __name__)

COOKIE_NAME = "access_token_cookie" 

@auth_bp.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return render_template("login.html", error="Usuário ou senha inválidos")

    try:
        conn = get_db_connection()
        user = conn.execute(
        "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        conn.close()
    except sqlite3.Error as e:
        logger.error("Error de conexão com o Banco de dados: %s", e)
        return render_template(
            "login.html",
            error="Não foi posivel acessar o sistema no momento. Tente novamente mais tarde."
        )
    

    if user is None or not check_password_hash(user["password_hash"], password):
        return render_template("login.html", error="Usuário ou senha inválidos")

    token = generate_token(user_id=user["id"], username=user["username"])

    response = make_response(redirect(url_for("agenda.agenda_page")))
    response.set_cookie(
        COOKIE_NAME,
        token,
        httponly=True,       
        samesite="Lax",      
        max_age=2 * 60 * 60 
    )
    return response