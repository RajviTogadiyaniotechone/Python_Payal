



import sqlite3
import pickle
import os
from datetime import datetime
import pytz

# Path for the database file
db_path = os.path.join('data', 'visitors.db')

# Ensure the data folder exists
os.makedirs('data', exist_ok=True)

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create tables if they do not exist
def create_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS unique_persons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id TEXT UNIQUE,
            name TEXT,
            face_encoding BLOB
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS detections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id TEXT,
            timestamp DATETIME 
        )
    ''')

    conn.commit()

# Insert a new person or update if they already exist
def insert_unique_person(person_id, name, face_encoding):
    try:
        cursor.execute('''
            INSERT OR IGNORE INTO unique_persons (person_id, name, face_encoding)
            VALUES (?, ?, ?)
        ''', (person_id, name, face_encoding))
        conn.commit()
    except Exception as e:
        print(f"[ERROR] Insert unique: {e}")

# Insert detection record for a person
def insert_detection(person_id):
    ist = pytz.timezone('Asia/Kolkata')
    ist_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO detections (person_id, timestamp) VALUES (?, ?)", (person_id, ist_time))
    conn.commit()

# Retrieve all known encodings from the database
def get_all_encodings():
    cursor.execute('SELECT person_id, face_encoding FROM unique_persons')
    rows = cursor.fetchall()
    return rows

# Close database connection
def close_db():
    conn.close()


