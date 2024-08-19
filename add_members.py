
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
        except Error:
            print({Error})

def add_workout_session(member_id, session_id, date, time, activity):
    conn = connection()
    if conn is not None:  
        try:
            cursor = conn.cursor()
            query = "INSERT INTO WorkoutSessions Values (%s, %s, %s, %s, %s)"
            values = member_id, session_id, date, time, activity
            cursor.execute(query, values)
            conn.commit()
            print("New workout session added")
        except Error:
            print({Error})

def update_member_age(member_id, new_age):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "UPDATE Members SET age = %s WHERE id = %s"
            values = new_age, member_id
            cursor.execute(query, values)
            conn.commit()
            print("Member age updated")
        except Error:
            print({Error})


def delete_workout_session(session_id):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(query, session_id)
            conn.commit()
            print("Session deleted")
        except Error:
            print({Error})


update_member_age(1,38)
