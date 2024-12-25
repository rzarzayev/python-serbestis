import sqlite3

def create_database():
    conn = sqlite3.connect("honeypot.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attacks (
            id INTEGER PRIMARY KEY,
            ip TEXT,
            port INTEGER,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_attack(ip, port, timestamp):
    conn = sqlite3.connect("honeypot.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attacks (ip, port, timestamp) VALUES (?, ?, ?)", (ip, port, timestamp))
    conn.commit()
    conn.close()

# Nümunə məlumat əlavə edin
create_database()
log_attack("192.168.1.1", 8080, "2024-12-25 15:30:00")
