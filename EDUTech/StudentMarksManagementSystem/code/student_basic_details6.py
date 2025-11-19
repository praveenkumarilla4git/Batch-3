import mysql.connector
from mysql.connector import Error

db_host = input("Enter the host/IP address of the studentapp-db MySQL server: ")

db_config = {
    'host': db_host,
    'user': 'admin',
    'password': 'database@1',
    'database': 'school_db',
    'port': 3306
}

school_name = input("Enter School Name: ")
school_branch = input("Enter School Branch: ")
student_name = input("Enter Student Name: ")
student_roll = input("Enter Student Roll Number: ")

try:
    conn = mysql.connector.connect(**db_config)
    if conn.is_connected():
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO student_basic (school_name, school_branch, student_name, student_roll) VALUES (%s, %s, %s, %s)",
            (school_name, school_branch, student_name, student_roll)
        )
        conn.commit()
        print("Details saved successfully!")
except Error as e:
    print(f"Error while connecting to MySQL: {e}")
finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
