class Student:
    def __init__(self):
        stu_ID = ""
        name=""
        dob=""
        major=""
    def create_student(self):
        self.stu_ID = input("Enter the student's ID:")
        self.name = input("Enter the name of the student:")
        self.dob = input("Enter the DOB of the student:")
        self.major = input("Enter the major of the student:")
    def display_student_details(self):
        print(self.name)
        print(self.stu_ID)
        print(self.dob)
        print(self.major)




stud1 = Student()
stud1.create_student()
stud1.display_student_details()
