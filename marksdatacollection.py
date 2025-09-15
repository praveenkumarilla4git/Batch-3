# First ask how many students are present in the class
num_students = int(input("Enter the total number of students in the class: "))
print(f"number of students {num_students}")
# to capture the data we create a container which is a dictionary
all_students_data = []
#student_name = input("Enter the student's name: ")

# we will use loops concept to understand how the indidual student data can be taken as input from user

for i in range(num_students):
    print(f"Enter details for student {i+1}")

    #Student details --> student_name
    student_name = input("Enter the student name: ")
    roll_number = input("Enter the roll number: ")
    student_class = input("Enter the student's class: ")

    #Create a dictionary to store student data into current individual dict
    student_data = {
        "name": student_name,
        "roll_number": roll_number,
        "class_name": student_class

    }

    # Add the students dict to the list

    all_students_data.append(student_data)

# Display all collected student details properly
print("\n --- All Student Details ----")
for student in all_students_data:
    print(f"\n\n\nName: {student['name']}")
    print(f"\nRoll Number: {student['roll_number']}")
    print(f"\nClass: {student['class_name']}")

