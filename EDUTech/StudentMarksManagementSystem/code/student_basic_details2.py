import mysql.connector
import sys

# Get EC2 public IP from command-line argument
if len(sys.argv) < 2:
    print("Usage: python student_basic_details.py <EC2_PUBLIC_IP>")
    sys.exit(1)

db_host = sys.argv[1]  # First argument after script name

# Ask for student details
name = input("Enter the student's name: ")
roll_number = input("Enter the student's roll number: ")
student_class = input("Enter the student's class: ")

# Print the collected information
print("\nStudent Details:")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Class: {student_class}")

# Ask for subject marks for Unit 1
english_marks = int(input("Enter marks scored in English (out of 25): "))
hindi_marks = int(input("Enter marks scored in Hindi (out of 25): "))
telugu_marks = int(input("Enter marks scored in Telugu (out of 25): "))
maths_marks = int(input("Enter marks scored in Maths (out of 25): "))
science_marks = int(input("Enter marks scored in Science (out of 25): "))
social_marks = int(input("Enter marks scored in Social (out of 25): "))

# Print all details including marks
print("\nStudent Details with Unit 1 Marks:")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Class: {student_class}")
print("Marks in Unit 1:")
print(f"English: {english_marks} / 25")
print(f"Hindi: {hindi_marks} / 25")
print(f"Telugu: {telugu_marks} / 25")
print(f"Maths: {maths_marks} / 25")
print(f"Science: {science_marks} / 25")
print(f"Social: {social_marks} / 25")

# Ask for subject marks for Unit 2
print("\nEnter marks for Unit 2:")
english_marks_unit2 = int(input("English (out of 25): "))
hindi_marks_unit2 = int(input("Hindi (out of 25): "))
telugu_marks_unit2 = int(input("Telugu (out of 25): "))
maths_marks_unit2 = int(input("Maths (out of 25): "))
science_marks_unit2 = int(input("Science (out of 25): "))
social_marks_unit2 = int(input("Social (out of 25): "))

# Ask for subject marks for Quarterly exam
print("\nEnter marks for Quarterly exam:")
english_marks_quarterly = int(input("English (out of 25): "))
hindi_marks_quarterly = int(input("Hindi (out of 25): "))
telugu_marks_quarterly = int(input("Telugu (out of 25): "))
maths_marks_quarterly = int(input("Maths (out of 25): "))
science_marks_quarterly = int(input("Science (out of 25): "))
social_marks_quarterly = int(input("Social (out of 25): "))

# Print all marks
print("\nAll Marks Entered:")
print("Unit 1:")
print(f"English: {english_marks} / 25, Hindi: {hindi_marks} / 25, Telugu: {telugu_marks} / 25, Maths: {maths_marks} / 25, Science: {science_marks} / 25, Social: {social_marks} / 25")

print("Unit 2:")
print(f"English: {english_marks_unit2} / 25, Hindi: {hindi_marks_unit2} / 25, Telugu: {telugu_marks_unit2} / 25, Maths: {maths_marks_unit2} / 25, Science: {science_marks_unit2} / 25, Social: {social_marks_unit2} / 25")

print("Quarterly Exam:")
print(f"English: {english_marks_quarterly} / 25, Hindi: {hindi_marks_quarterly} / 25, Telugu: {telugu_marks_quarterly} / 25, Maths: {maths_marks_quarterly} / 25, Science: {science_marks_quarterly} / 25, Social: {social_marks_quarterly} / 25")

# Connect to MySQL
conn = mysql.connector.connect(
    host=db_host,
    user='root',  # Change if you use another MySQL user
    password='database@1',  # Change to your MySQL password
    database='school_db'
)

cursor = conn.cursor()

# Insert Unit 1 marks
sql = "INSERT INTO student_marks (name, roll_number, class, unit, english, hindi, telugu, maths, science, social) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
values_unit1 = (name, roll_number, student_class, "Unit 1", english_marks, hindi_marks, telugu_marks, maths_marks, science_marks, social_marks)
cursor.execute(sql, values_unit1)
conn.commit()

# Insert Unit 2 marks
values_unit2 = (name, roll_number, student_class, "Unit 2", english_marks_unit2, hindi_marks_unit2, telugu_marks_unit2, maths_marks_unit2, science_marks_unit2, social_marks_unit2)
cursor.execute(sql, values_unit2)
conn.commit()

# Insert Quarterly marks
values_quarterly = (name, roll_number, student_class, "Quarterly", english_marks_quarterly, hindi_marks_quarterly, telugu_marks_quarterly, maths_marks_quarterly, science_marks_quarterly, social_marks_quarterly)
cursor.execute(sql, values_quarterly)
conn.commit()

print("\nAll marks submitted successfully to database!")

cursor.close()
conn.close()
