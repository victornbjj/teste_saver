import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
from app.database import init_db, get_db_connection

load_dotenv()

def seed():
    init_db()  

    conn = get_db_connection()
    email = os.getenv("TEST_USER_EMAIL")
    password = os.getenv("TEST_USER_PASSWORD")
    password_hash = generate_password_hash(password)


    conn.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (email, password_hash)
    )
    conn.commit()
    conn.close()
    print("Banco inicializado e usuário de teste criado")

if __name__ == "__main__":
    seed()