import sqlite3

conn = sqlite3.connect('Courses.db')
c = conn.cursor()

def create_table():
    try:
        conn = sqlite3.connect('Courses.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Courses (course_ID INTEGER PRIMARY KEY, name TEXT, duration TEXT, course_format TEXT, language TEXT, price TEXT)")
        conn.commit()
    except sqlite3.Error as e:
        print("Error creating table:", e)
    finally:
        conn.close()


def insert_course(course_ID, name, duration, course_format, language, price):
    try:
        conn = sqlite3.connect('Courses.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Courses (course_ID, name, duration, course_format, language, price) VALUES (?, ?, ?, ?, ?, ?)",
                (course_ID, name, duration, course_format, language, price))
        conn.commit()
    except sqlite3.Error as e:
        print("Error inserting course:", e)
    finally:
        conn.close()

def search_courses(query):
    try:
        conn = sqlite3.connect("Courses.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Courses WHERE course_ID = ?", (query,))
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print("Error searching courses:", e)
    finally:
        conn.close()


def fetch_all_ids():
    try:
        conn = sqlite3.connect("Courses.db")
        cursor = conn.cursor()
        cursor.execute("SELECT course_id FROM Courses")
        ids = cursor.fetchall()
        if ids:
            return [i[0] for i in ids]
        else:
            return []
    except sqlite3.Error as e:
        print("Error fetching IDs:", e)
    finally:
        conn.close()


def id_exists(course_id):
    try:
        conn = sqlite3.connect("Courses.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Courses WHERE course_id = ?", (course_id,))
        result = cursor.fetchone()
        return result[0] > 0
    except sqlite3.Error as e:
        print("Error checking ID existence:", e)
    finally:
        conn.close()

create_table()