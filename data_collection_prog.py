# Create a List to store student marks
marks = [92, 88, 95, 78, 90]
print(f"Student marks: {marks}")
marks.append(85)
print(f"Student marks: {marks}")

print("=" * 50)

# Create a TUPLE to store the students personal info which is unchangeble
personal_info = ("Sai", 15, "Class 10A")
print(f"personal_info (Tuple): {personal_info}")

print("=" * 50)


# Create a Dictionary to store subjects and their corresponding scores.
# Dictionaries use key-value pairs for structed data lookup
subjects = {
    "Maths": 92,
    "Science": 88,
    "Social": 95,
    "English": 78,
    "Telugu": 85
}
print((f"Subject scores (Dictionaries): {subjects}"))

print("=" * 50)

#Create a SET to store a student's unique IDs

student_ids = {101, 102, 103, 104}
print(student_ids)