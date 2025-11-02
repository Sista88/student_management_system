# src/student_manager.py

import os

# Path to store student data
DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/students.txt')

def add_student():
    #"""Add a new student and save to the students.txt file."""
    print("\n--- Add New Student ---")
    
    # Take input from user
    roll_no = input("Enter Roll Number: ").strip()
    name = input("Enter Name: ").strip()
    marks = input("Enter Marks (comma-separated for subjects, e.g., 75,80,90): ").strip()
    
    # Prepare student record as a string
    student_record = f"{roll_no}|{name}|{marks}\n"
    
    # Append to the file
    with open(DATA_FILE, "a") as file:
        file.write(student_record)
    
    print(f"✅ Student {name} added successfully!")


def view_students():
    #"""Read and display all students from the students.txt file."""
    print("\n--- List of Students ---")
    
    # Check if file exists
    if not os.path.exists(DATA_FILE):
        print("No students found. The data file is empty.")
        return
    
    # Read the file
    with open(DATA_FILE, "r") as file:
        students = file.readlines()
    
    # If file is empty
    if not students:
        print("No students found.")
        return
    
    # Display students in a table-like format
    print(f"{'Roll No':<10}{'Name':<20}{'Marks'}")
    print("-" * 40)
    for student in students:
        roll_no, name, marks = student.strip().split("|")
        print(f"{roll_no:<10}{name:<20}{marks}")
        

def search_student():
    #"""Search for a student by roll number."""
    print("\n--- Search Student ---")
    roll_no_to_search = input("Enter Roll Number to search: ").strip()

    if not os.path.exists(DATA_FILE):
        print("No students found. The data file is empty.")
        return

    with open(DATA_FILE, "r") as file:
        students = file.readlines()

    found = False
    for student in students:
        roll_no, name, marks = student.strip().split("|")
        if roll_no == roll_no_to_search:
            print(f"Student Found: Roll No: {roll_no}, Name: {name}, Marks: {marks}")
            found = True
            break

    if not found:
        print(f"No student found with Roll Number {roll_no_to_search}.")


def update_student():
    #"""Update details of an existing student by roll number."""
    print("\n--- Update Student ---")
    roll_no_to_update = input("Enter Roll Number to update: ").strip()

    if not os.path.exists(DATA_FILE):
        print("No students found. The data file is empty.")
        return

    with open(DATA_FILE, "r") as file:
        students = file.readlines()

    updated = False
    new_students = []

    for student in students:
        roll_no, name, marks = student.strip().split("|")
        if roll_no == roll_no_to_update:
            print(f"Current details: Name: {name}, Marks: {marks}")
            new_name = input("Enter new name (press enter to keep current): ").strip()
            new_marks = input("Enter new marks (comma-separated, press enter to keep current): ").strip()
            
            # Keep old values if input is empty
            if not new_name:
                new_name = name
            if not new_marks:
                new_marks = marks

            new_students.append(f"{roll_no}|{new_name}|{new_marks}\n")
            updated = True
            print(f"✅ Student {roll_no} updated successfully!")
        else:
            new_students.append(student)

    # Save updated data back to the file
    with open(DATA_FILE, "w") as file:
        file.writelines(new_students)

    if not updated:
        print(f"No student found with Roll Number {roll_no_to_update}.")


def delete_student():
    #"""Delete a student by roll number."""
    print("\n--- Delete Student ---")
    roll_no_to_delete = input("Enter Roll Number to delete: ").strip()

    if not os.path.exists(DATA_FILE):
        print("No students found. The data file is empty.")
        return

    with open(DATA_FILE, "r") as file:
        students = file.readlines()

    new_students = []
    deleted = False

    for student in students:
        roll_no, name, marks = student.strip().split("|")
        if roll_no == roll_no_to_delete:
            deleted = True
            print(f"✅ Student {name} (Roll No: {roll_no}) deleted successfully!")
            continue  # Skip adding this student to new list
        new_students.append(student)

    if deleted:
        with open(DATA_FILE, "w") as file:
            file.writelines(new_students)
    else:
        print(f"No student found with Roll Number {roll_no_to_delete}.")


def calculate_grades():
    #"""Calculate and display grades for all students based on average marks."""
    print("\n--- Calculate Grades ---")

    if not os.path.exists(DATA_FILE):
        print("No students found. The data file is empty.")
        return

    with open(DATA_FILE, "r") as file:
        students = file.readlines()

    if not students:
        print("No students found.")
        return

    print(f"{'Roll No':<10}{'Name':<20}{'Average':<10}{'Grade'}")
    print("-" * 50)

    for student in students:
        roll_no, name, marks_str = student.strip().split("|")
        # Convert marks to a list of floats
        try:
            marks = [float(m) for m in marks_str.split(",")]
        except ValueError:
            print(f"{roll_no:<10}{name:<20}Invalid marks format")
            continue

        avg = sum(marks) / len(marks)

        # Simple grading logic
        if avg >= 90:
            grade = "A+"
        elif avg >= 80:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "F"

        print(f"{roll_no:<10}{name:<20}{avg:<10.2f}{grade}")

