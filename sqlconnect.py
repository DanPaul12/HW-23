import mysql.connector
from mysql.connector import Error

db_name = "fitness_center_db"
user = "root"
password = "thegoblet2"
host = "localhost"

def connection():
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
    except Error as e:
        print("Error: {e}")
    finally:
        conn.close()