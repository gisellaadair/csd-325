import json

# Step 1: Load the JSON file
with open("student.json", "r") as file:
    students = json.load(file)

# Step 2: Function to print student list
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")
    print("\n")  # extra line for readability

# Step 3: Notify user about the original list
print("Original Student List:")
print_students(students)

# Step 4: Append your info
my_student = {
    "F_Name": "Gisella",
    "L_Name": "Adair",
    "Student_ID": 99999,  # fictional ID
    "Email": "g.adair@example.com"
}

students.append(my_student)

# Step 5: Notify user about the updated list
print("Updated Student List:")
print_students(students)

# Step 6: Save updated list back to JSON
with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

print("The student.json file has been updated.")
