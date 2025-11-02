# src/main.py

from student_manager import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    calculate_grades
)

def show_menu():
    #"""Display the main menu options to the user."""
    print("\n===== Student Management System =====")
    print("1. Add new student")
    print("2. View all students")
    print("3. Search student by roll number")
    print("4. Update student details")
    print("5. Delete a student")
    print("6. Calculate and display grades")
    print("7. Exit")

def main():
    #"""Main function to handle user input and menu navigation."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            calculate_grades()
        elif choice == '7':
            print("Exiting program... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
