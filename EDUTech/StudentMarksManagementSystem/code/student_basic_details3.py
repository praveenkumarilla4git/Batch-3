import mysql.connector

# Ask user for the DB host/IP
db_host = input("Enter the host/IP address of the studentapp-db MySQL server: ")

# Database connection config
db_config = {
    'host': db_host,
    'user': 'root',
    'password': 'database@1',
    'database': 'school_db',
    'port': 3306
}

# Collect basic details from user
school_name = input("Enter School Name: ")
school_branch = input("Enter School Branch: ")
student_name = input("Enter Student Name: ")
student_roll = input("Enter Student Roll Number: ")

# Insert collected data into DB
conn = mysql.connector.connect(**db_config)
cur = conn.cursor()
cur.execute(
    "INSERT INTO student_basic (school_name, school_branch, student_name, student_roll) VALUES (%s, %s, %s, %s)",
    (school_name, school_branch, student_name, student_roll)
)
conn.commit()
cur.close()
conn.close()

print("Details saved successfully!")
