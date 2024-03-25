
class Person:
    def __init__(self,a,b,c,d):
        self.__name = ""
        self.__dob = ""
        self.__gender = ""
        self.__city = ""
    def display(self):
        print("PersonName: ",self.__name)
        print("PersonDOB: ",self.__dob)
        print("PersonGender: ",self.__gender)
        print("PersonCity: ",self.__city)
class Student(Person):
    def __init__(self,a,b,c,d,id,gradYr,nncc):
        Person.__init__(self,a,b,c,d)
        self.__stuID = ""
        self.__gradYr = ""
        self.__numCourses = nncc
    def display(self):
        print(Person.display(self))
        print("StudentID: ",self.__stuID)
        print("GradYR: ",self.__gradYr)
        print("NumOfCourses: ",self.__numCourses)
        print("")

list_courses = ["OOP","LinAlg","Psychology"]
s1 = Student("Sky","2012","M","Siloam","123","2025","4")
s2 = Student("Issy","1998","F","Rogers","312","2024","5")
s1.display()
s2.display()


