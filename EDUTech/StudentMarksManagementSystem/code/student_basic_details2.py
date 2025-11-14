import mysql.connector

# Ask user for MySQL host (EC2 Public IP)
db_host = input("Enter your EC2 Public IP or MySQL Host: ")

# Ask for student details
name = input("Enter the student's name: ")
roll_number = input("Enter the student's roll number: ")
student_class = input("Enter the student's class: ")

print("\nStudent Details:")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Class: {student_class}")

# Unit 1 marks
english_marks = int(input("English Unit 1 (out of 25): "))
hindi_marks = int(input("Hindi Unit 1 (out of 25): "))

# Connect to MySQL Database
conn = mysql.connector.connect(
    host=db_host,
    user='admin',          # your MySQL username
    password='database@1', # your MySQL password
    database='school_db'
)

cursor = conn.cursor()

# Insert into database (Unit 1)
sql = """INSERT INTO student_marks 
(name, roll_number, class, unit, english, hindi, telugu, maths, science, social) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
cursor.execute(sql, (name, roll_number, student_class, "Unit 1",
                     english_marks, hindi_marks, telugu_marks,
                     maths_marks, science_marks, social_marks))
conn.commit()

# Insert Unit 2
cursor.execute(sql, (name, roll_number, student_class, "Unit 2",
                     english_u2, hindi_u2, telugu_u2,
                     maths_u2, science_u2, social_u2))
conn.commit()

# Insert Quarterly
cursor.execute(sql, (name, roll_number, student_class, "Quarterly",
                     english_q, hindi_q, telugu_q,
                     maths_q, science_q, social_q))
conn.commit()

print("\nAll marks submitted successfully!")

cursor.close()
conn.close()
