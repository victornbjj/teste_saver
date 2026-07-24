import os
import sys
import tempfile
from pathlib import Path

import pytest
from werkzeug.security import generate_password_hash

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app import create_app
from app.database import init_db, get_db_connection


@pytest.fixture
def app(monkeypatch):
    # Cria um banco SQLite temporário para cada teste e garante que o app use esse arquivo.
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        db_path = tmp.name

    monkeypatch.setenv("DATABASE_PATH", db_path)
    monkeypatch.setenv("JWT_SECRET_KEY", "test-secret")

    app = create_app()
    app.config.update(TESTING=True)

    with app.app_context():
        init_db()
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            ("medico", generate_password_hash("senha123")),
        )
        conn.commit()
        conn.close()

    yield app

    os.remove(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


def test_login_com_credenciais_validas(client):
    # Valida que o login bem-sucedido redireciona para a agenda e define o cookie JWT.
    response = client.post(
        "/login",
        data={"username": "medico", "password": "senha123"},
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/agenda")
    assert "access_token_cookie" in response.headers.get("Set-Cookie", "")


def test_login_com_credenciais_invalidas(client):
    # Valida que credenciais inválidas retornam o formulário de login com mensagem genérica.
    response = client.post(
        "/login",
        data={"username": "medico", "password": "senha_errada"},
        follow_redirects=False,
    )

    assert response.status_code == 200
    assert "Usuário ou senha inválidos".encode("utf-8") in response.data
    lower_body = response.data.lower().decode("utf-8", errors="ignore")
    assert "usuário" in lower_body or "usuario" in lower_body
    assert "senha" in lower_body


def test_agenda_sem_autenticacao_redireciona_para_login(client):
    # Valida que o acesso protegido à agenda sem cookie redireciona para a página de login.
    response = client.get("/agenda", follow_redirects=False)

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/login")


def test_buscar_agendamentos_quando_api_falha_retorna_erro(monkeypatch):
    # Valida que falhas de rede em buscar_agendamentos() retornam erro sem levantar exceção.
    from app.agenda import client as agenda_client
    import requests

    def fake_get(*args, **kwargs):
        raise requests.exceptions.ConnectionError("falha")

    monkeypatch.setattr(agenda_client.requests, "get", fake_get)

    dados, erro = agenda_client.buscar_agendamentos()

    assert dados == []
    assert erro is not None
