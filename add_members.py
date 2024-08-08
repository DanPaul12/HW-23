from sqlconnect import connection 
from mysql.connector import Error

connection()

def add_member(id, name, age):
    try:
        cursor = cursor.execute()
        query = "INSERT INTO Members Values (%s, %s, %s)"
        values = id, name, age
        cursor(query, values)
    except Error as e:
        print("Error: {e}")
    finally: