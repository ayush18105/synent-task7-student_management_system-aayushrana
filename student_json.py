import json

FILE_NAME = "students.json"


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_student():
    students = load_data()

    student = {
        "id": input("Enter Student ID: "),
        "name": input("Enter Name: "),
        "age": input("Enter Age: "),
        "course": input("Enter Course: ")
    }

    students.append(student)
    save_data(students)

    print("\nStudent Added Successfully!")


def view_students():
    students = load_data()

    if len(students) == 0:
        print("\nNo Students Found!")
        return

    print("\n----- STUDENT LIST -----")

    for student in students:
        print(f"""
ID     : {student['id']}
Name   : {student['name']}
Age    : {student['age']}
Course : {student['course']}
-------------------------
""")


def update_student():
    students = load_data()

    student_id = input("Enter Student ID to Update: ")

    found = False

    for student in students:
        if student["id"] == student_id:

            student["name"] = input("New Name: ")
            student["age"] = input("New Age: ")
            student["course"] = input("New Course: ")

            found = True
            break

    if found:
        save_data(students)
        print("\nStudent Updated Successfully!")
    else:
        print("\nStudent Not Found!")

def delete_student():

    students = load_data()

    student_id = input("Enter Student ID to Delete: ")

    new_students = []

    found = False

    for student in students:
        if student["id"] != student_id:
            new_students.append(student)
        else:
            found = True

    if found:
        save_data(new_students)
        print("\nStudent Deleted Successfully!")
    else:
        print("\nStudent Not Found!")


while True:

    print("\n====== STUDENT MANAGEMENT SYSTEM ======")

    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice!")