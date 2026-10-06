import sqlite3


def create_database():

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    conn.commit()
    conn.close()


def register_student(username, password):

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    try:

        cursor.execute(
            "INSERT INTO students (username, password) VALUES (?, ?)",
            (username, password)
        )

        conn.commit()
        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conn.close()


def login_student(username, password):

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE username = ? AND password = ?",
        (username, password)
    )

    student = cursor.fetchone()

    conn.close()

    return student