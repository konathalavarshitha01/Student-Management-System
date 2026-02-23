import json
import os

FILE_NAME = "students.json"

# Load existing data
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

# Save data to file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file)

students = load_students()

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    students[roll] = {"Name": name, "Marks": marks}
    save_students(students)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No records found.")
    else:
        for roll, data in students.items():
            print(f"Roll: {roll}, Name: {data['Name']}, Marks: {data['Marks']}")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        save_students(students)
        print("Student deleted.")
    else:
        print("Student not found.")

while True:
    print("\n1.Add Student\n2.View Students\n3.Delete Student\n4.Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice")