students = {}

def add_student():
    name = input("Name: ")
    grade = input("Grade: ")
    attendance = input("Attendance: ")
    students[name] = {"grade": grade, "attendance": attendance}

def view_students():
    for name, info in students.items():
        print(name, info)

add_student()
view_students()
