class Student:
    index = 0

    def __init__(self, name="asdf", student_number=1111, department="fdas"):
        self.name = name
        self.student_number = student_number
        self.department = department
        Student.index += 1
        print("create student!")

    def welcome(self):
        print("hi, " + self.name)

    def print_info(self):
        print(self.index, self.name, self.department, self.student_number)


class Professor(Student):
    def check_in(self):
        print("출췤")
