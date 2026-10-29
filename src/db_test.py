from database import get_connection
from datetime import datetime

conn = get_connection()

attractions = conn.execute("SELECT * FROM attractions;").fetchall()

for attraction in attractions:
    print(attraction)

conn.close()