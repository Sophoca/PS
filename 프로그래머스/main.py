from classA import Student, Professor

studentA = Student("엉으니", 202126631, "교시공")
studentA.print_info()
print(studentA.__dict__)

studentB = Student("성빈", 201720813, "소웨")
studentB.print_info()
print(studentA.index, studentB.index)
studentA.index = 500

studentC = Student()
studentC.print_info()
print(studentA.index, studentB.index, studentC.index)

prof = Professor("교수님", 1111, "다산")
prof.print_info()
prof.check_in()
