from sqlconnect import connection 
from mysql.connector import Error


def add_member(id, name, age):
    conn = connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO Members Values (%s, %s, %s)"
            values = id, name, age
            cursor.execute(query, values)
            conn.commit()
            print("New member added")
        except Error as e:
            print("Error: {e}")
        
add_member(7, "Bobby Flake", 45)