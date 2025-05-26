import sqlite3

def init_db():
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_task(task, date):
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task, date) VALUES (?, ?)", (task, date))
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    conn.close()
    return [{"id": r[0], "task": r[1], "date": r[2]} for r in rows]

def delete_task(task_id):
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
