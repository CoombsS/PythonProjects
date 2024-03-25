import pickle

class courseGrades:
    def __init__(self):
        self.cname = ""
        self.stuID = []
        self.stuGrade = []
    def addStu(self):
        self.cname = input("Please enter the course name: ")
        for i in range (1,5):
            self.stuID = input("Please enter the stuID")
            self.stuGrade = input("Please enter the stuGrade")
    def save(self):
        f = open('Grades_Info.dat','ab')
        pickle.dump(u1, f)
        f.close()
    def display(self):
        f = open('Grades_Info.dat','rb',)
        while 1:
            try:
                data = pickle.load(f)
                print(data.cname)
                for stuID in data.cname:
                    print(stuID)
                    for stuGrade in data.cname:
                        print(stuGrade)
            except (EOFError):
                break

u1 = courseGrades()
u1.addStu()
u1.save()
u1.display()