# Juan Cardenas
# 11/1/2026
# Module 8.2 Assignment
# Purpose: To create a program that reads a JSON file containing student information,
# displays the original list, adds a new student, and saves the
# updated list back to the JSON file.

import json


# Function to display the student list
def print_students(students):
    for student in students:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']} , "
            f"Email = {student['Email']}"
        )

# Load the original student list from the JSON file
with open("Student.json", "r") as file:
    students = json.load(file)

# Display the original student list
print("Original Student List:")
print_students(students)

# Add a new student to the list
students.append({
    "F_Name": "Juan",
    "L_Name": "Cardenas",
    "Student_ID": 78901,
    "Email": "juacardenas@my365.bellevue.edu"
})

# Display the updated student list
print("\nUpdated Student List:")
print_students(students)

# Save the updated student list to the JSON file
with open("Student.json", "w") as file:
    json.dump(students, file, indent=4)

# Notify the user that the file was updated
print("\nStudent.json has been updated successfully.")
