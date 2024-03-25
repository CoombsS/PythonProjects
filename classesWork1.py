
class Student:
    def __init__(self):
        name = ""
        stuID = ""
        dob = ""
        major = ""
    def createStudent(self):
        self.name = input("Please enter the student's name:")
        self.stuID = input("Please enter the student's ID:")
        self.dob = input("Please enter the date of birth:")
        self.major = input("Please enter the student's major:")
    def removeStudent(self):
        re = input("Please enter the student you would like to remove: ")
        Student.remove(re)
    def displayStudent(self):
        dS = input("Enter the student you would like to view: ")
        print(dS)
    def displayAllStudents(self):
        print(self.name)
        print(self.stuID)
        print(self.dob)
        print(self.major)
class Faculty:
    def __init__(self):
        name = ""
        facID = ""
        dob = ""
        depart = ""






#stud1=Student()
#stud1.createStudent()
#stud1.displayStudent()

while 1:
    count = 1
    print("1. Add a new student.")
    print("2. Display a certain student.")
    print("3. Display all students.")
    print("4. Modify a student.")
    print("5. Add a new faculty.")
    print("6. Display a certain faculty.")
    print("7. Display all faculty.")
    print("8. Modify a faculty.")
    print("9. Exit.")
    ans = input("What is your decision?: ")
    if ans == 1:
        stud1 = Student()
        stud1.createStudent()
        stud1.displayStudent()
    if ans == 2:
        Student = "STUD" + str(count)
        Student.createStudent()
        count = count + 1
