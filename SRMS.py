# Student Record Management System

students = {}

def create_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
    print("Student added successfully!")

def read_students():
    if not students:
        print("No records found.")
    else:
        for name, marks in students.items():
            print(name, ":", marks)

def update_student():
    name = input("Enter student name to update: ")
    if name in students:
        marks = int(input("Enter new marks: "))
        students[name] = marks
        print("Record updated!")
    else:
        print("Student not found.")

def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print("Record deleted!")
    else:
        print("Student not found.")

while True:
    print("\n1. Create\n2. Read\n3. Update\n4. Delete\n5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        create_student()
    elif choice == '2':
        read_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice")