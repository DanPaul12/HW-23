from sqlconnect import connection 
from mysql.connector import Error


def add_member(id, name, age):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO Members Values (%s, %s, %s)"
            values = id, name, age
            cursor.execute(query, values)
            conn.commit()
            print("New member added")
        except Error as e:
            print("Error: {e}")
        



def delete_workout_session(session_id):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
            values = session_id
            cursor.execute(query, values)
            print("Session deleted")
        except:
            pass

delete_workout_session("2")