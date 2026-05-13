import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import json
from datetime import datetime
from contextlib import contextmanager

DATABASE = 'medreport.db'



@contextmanager
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with get_db() as conn:
        c = conn.cursor()
        
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        c.execute('''
            CREATE TABLE IF NOT EXISTS reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                filename TEXT NOT NULL,
                upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                analysis_data TEXT NOT NULL,
                health_score INTEGER,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        conn.commit()

def create_user(username, email, password):
    with get_db() as conn:
        c = conn.cursor()
        try:
            c.execute(
                'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                (username, email, generate_password_hash(password))
            )
            conn.commit()
            return True, "User created successfully"
        except sqlite3.IntegrityError:
            return False, "Username or email already exists"

def verify_user(username, password):
    with get_db() as conn:
        c = conn.cursor()
        c.execute(
            'SELECT * FROM users WHERE username = ?',
            (username,)
        )
        user = c.fetchone()
        if user and check_password_hash(user['password'], password):
            return dict(user)
        return None

def save_report(user_id, filename, analysis_data, health_score):
    with get_db() as conn:
        c = conn.cursor()
        c.execute(
            '''INSERT INTO reports (user_id, filename, analysis_data, health_score) 
               VALUES (?, ?, ?, ?)''',
            (user_id, filename, json.dumps(analysis_data), health_score)
        )
        conn.commit()
        return c.lastrowid

def get_user_reports(user_id):
    with get_db() as conn:
        c = conn.cursor()
        c.execute(
            '''SELECT id, filename, upload_date, health_score 
               FROM reports WHERE user_id = ? ORDER BY upload_date DESC''',
            (user_id,)
        )
        return [dict(row) for row in c.fetchall()]

def get_report_data(report_id, user_id):
    with get_db() as conn:
        c = conn.cursor()
        c.execute(
            '''SELECT analysis_data FROM reports 
               WHERE id = ? AND user_id = ?''',
            (report_id, user_id)
        )
        row = c.fetchone()
        if row:
            return json.loads(row['analysis_data'])
        return None

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully")
