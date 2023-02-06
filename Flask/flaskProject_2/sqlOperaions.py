
import sqlite3 as sql
conn = sql.connect('onlineclasses.sqlite2')
curs = conn.cursor()

def createCourseTable():
    curs.execute("create table course(cno number primary key, c_name text, faculty_name text, class_date date, class_time text, fee real, duration number)")
    conn.close()
    print("table is created")

createCourseTable()


