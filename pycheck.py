import mysql.connector

conn = mysql.connector.connect(host = "localhost",user = 'root',password = '1234' , database = "attendance_manager")
my_cursor = conn.cursor()
my_cursor.execute("select * from student_data")