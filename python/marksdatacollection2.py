# Student Marks Data Program for Multiple Students

# First, ask how many students are in the class
while True:
    try:
        num_students = int(input("Enter the total number of students in the class: "))
        if num_students > 0:
            break
        else:
            print("Please enter a positive number of students.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"\nNumber of students: {num_students}")

# Create a list to hold data for all students
all_students_data = []

# Define the subjects
subjects = ["English", "Hindi", "Telugu", "Maths", "Science", "Social"]

# Loop through each student to collect their details and marks
for i in range(num_students):
    print(f"\n--- Enter details for student {i + 1} ---")

    # Get basic student details
    student_name = input("Enter the student name: ")
    roll_number = input("Enter the roll number: ")
    student_class = input("Enter the student's class: ")

    # Create a dictionary to store the current student's data
    student_data = {
        "name": student_name,
        "roll_number": roll_number,
        "class_name": student_class,
        "marks": {}  # A nested dictionary to store subject marks
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

    # Add total marks and percentage to the student's dictionary
    student_data["total_marks"] = total_marks
    student_data["percentage"] = percentage

    # Add the current student's data dictionary to the list
    all_students_data.append(student_data)
    print(student_data)

# Display all collected student details and marks
print("\n" + "=" * 40)
print("             STUDENT MARK SHEETS")
print("=" * 40)
for student in all_students_data:
    print(f"\nName: {student['name']}")
    print(f"Roll Number: {student['roll_number']}")
    print(f"Class: {student['class_name']}")
    print("-" * 20)

    # Display individual subject marks
    for subject, score in student['marks'].items():
        print(f"{subject:<10}: {score:>3}")  # Use f-string formatting to align text

    print("-" * 20)
    print(f"Total Marks: {student['total_marks']}")
    print(f"Percentage: {student['percentage']:.2f}%")  # Format percentage to two decimal places
    print("=" * 40)
