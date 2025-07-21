
# logger.py
import sqlite3
from datetime import datetime

# 🔹 SQLite Logging
def log_event_sqlite(event_type):
    conn = sqlite3.connect("logs.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS fire_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            event TEXT)
    """)
    cur.execute("INSERT INTO fire_logs (timestamp, event) VALUES (?, ?)",
                (datetime.now().isoformat(), event_type))
    conn.commit()
    conn.close()


# 🔹 Firebase Firestore Logging (optional)
try:
    import firebase_admin
    from firebase_admin import credentials, firestore
    import os

    if not firebase_admin._apps:
        cred = credentials.Certificate("firebase_config.json")
        firebase_admin.initialize_app(cred)

    db = firestore.client()

    def log_event_firebase(event_type):
        db.collection("fire_logs").add({
            "timestamp": datetime.now().isoformat(),
            "event": event_type
        })

except Exception as e:
    def log_event_firebase(event_type):
        print("Firebase not initialized:", e)
