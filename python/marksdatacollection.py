# First ask how many students are present in the class
num_students = int(input("Enter the total number of students in the class: "))
print(f"number of students {num_students}")
# to capture the data we create a container which is a dictionary
all_students_data = []
#student_name = input("Enter the student's name: ")
# Define the subjects
subjects = ["English", "Hindi", "Telugu", "Maths", "Science", "Social"]
# we will use loops concept to understand how the indidual student data can be taken as input from user

for i in range(num_students):
    print(f"Enter details for student {i+1}")

    #Student details --> student_name
    student_name = input("Enter the student name: ")
    roll_number = input("Enter the roll number: ")
    student_class = input("Enter the student's class: ")
    student_marks = input("Enter the student's marks: ")

    #Create a dictionary to store student data into current individual dict
    student_data = {
        "name": student_name,
        "roll_number": roll_number,
        "class_name": student_class,
        "marks": student_marks

    }

    # Loop through each subject to get the marks
    print("\nEnter marks for each subject (out of 100):")
    for subject in subjects:
        while True:
            try:
                score = int(input(f"Enter marks for {subject}: "))
                if 0 <= score <= 100:
                    student_data["marks"][subject] = score
                    break  # Valid score, exit inner loop
                else:
                    print("Invalid input. Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Calculate total marks and percentage for the student
    total_marks = sum(student_data["marks"].values())
    percentage = (total_marks / (len(subjects) * 100)) * 100

    # Add the students dict to the list

    all_students_data.append(student_data)

# Display all collected student details properly
print("\n --- All Student Details ----")
for student in all_students_data:
    print(f"\n\n\nName: {student['name']}")
    print(f"\nRoll Number: {student['roll_number']}")
    print(f"\nClass: {student['class_name']}")

