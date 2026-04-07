def main():

    students = {}

    while True:
        print("\n1. Add student")
        print("2. View student")
        print("3. Delete Student")
        print("4. Show All Students")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            course = input("Enter course: ")
            add_student(students, name, age, course)
        elif choice == "2":
            name = input("Enter name: ")
            view_student(students, name)
        elif choice == "3":
            name = input("Enter name: ")
            delete_student(students, name)
        elif choice == "4":
            show_all_students(students)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")



def add_student(students, name, age, course):
    """This function adds a student to the system!"""
    students[name] = {
        "age": age,
        "course":course
    }
    print(f"{name} added successfully!")



def view_student(students, name):
    """This function adds a student to the system!"""
    if name in students:
        print(f"Name: {name}")
        print(f"Age: {students[name]["age"]}")
        print(f"Course: {students[name]["course"]}")
    else:
        print("Student not found")



def delete_student(students, name):
    """This function adds a student to the system!"""
    if name in students:
        del students[name]
        print(f"Student {name} deleted successfully")
    else:
        print("Student not found")

def show_all_students(students):
    """This function adds a student to the system!"""
    if not students:
        print("No Student")
    else:
        for name, info in students.items():
            print(f"Name: {name}, Age: {info['age']}, Course: {info['course']}")



if __name__ == "__main__":
    main()
