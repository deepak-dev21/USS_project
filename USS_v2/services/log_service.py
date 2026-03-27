from services.db_service import get_connection

def add_log(message, type):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO logs (message,type) VALUES (?,?)",(message,type))
    conn.commit()
    conn.close()

def get_logs():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM logs")
    data = cur.fetchall()
    conn.close()
    return data