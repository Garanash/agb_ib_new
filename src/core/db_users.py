import sqlite3


def create_table_users():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT,
        mail TEXT UNIQUE,
        role TEXT NOT NULL,
        firstname TEXT NULL,
        lastname TEXT NULL,
        isactive BOOL DEFAULT FALSE,
        superuser BOOL DEFAULT FALSE,
        markfordelete BOOL DEFAULT FALSE)""")
    connection.commit()
    connection.close()


def search_user_by_username(username: str) -> tuple[str]:
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    connection.commit()
    connection.close()
    return user


def search_user_by_id(user_id: int) -> tuple[str]:
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    connection.commit()
    connection.close()
    return user


def search_password_by_username(username: str) -> str:
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    user_password = cursor.fetchone()
    connection.commit()
    connection.close()
    return user_password


def create_user(obj):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("""
            INSERT INTO users (
            username,password,mail,role,firstname,lastname,isactive,superuser)
            ) VALUES (?,?,?,?,?,?,?,?)
            """, (
        obj.username, obj.password, obj.mail, obj.role, obj.firstname, obj.lastname, obj.isactive, obj.superuser))
    connection.commit()
    connection.close()
