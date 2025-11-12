# student_basic_details.py

# Ask for student details
name = input("Enter the student's name: ")
roll_number = input("Enter the student's roll number: ")
student_class = input("Enter the student's class: ")

# Print the collected information
print("\nStudent Details:")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Class: {student_class}")


###############################################
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

##########################################################
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

