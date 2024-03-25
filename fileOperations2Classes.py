import pickle
class Student:
    def __init__(self):
        self.name = ""
        self.dob = ""
        self.courses = ""
    def get_details(self):
        self.name = input("Enter the name")
        self.dob = input("Enter the DOB")
        self.courses = input("Enter the courses")


#create obj for student class
s1 = Student()
s1.get_details()

s2 = Student()
s2.get_details()

#write the objects s1 s2 into a *.dat file
f = open('myStudent.dat','ab')
pickle.dump(s1, f)
pickle.dump(s2, f)
f.close()

#open the same dat file in read bianary mode
f = open('myStudent.dat','rb')

#use iterations to read the objects from the file and print the attributes of the class
while 1:
    try:
        data = pickle.load(f)
        print(data.name)
        print(data.dob)
        print(data.courses)
    except (EOFError):
        break
f.close()