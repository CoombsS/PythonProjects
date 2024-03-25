import matplotlib.pyplot as plt
import numpy as np
import pickle
class course_grades:
    def __init__(self):
        self.course_name = ""
        self.stu_ID = []
        self.stu_grades = []
    def get_values(self):
        self.course_name = input("Enter course name: ")
        for i in range (1,21):
            self.stu_ID.append(i)
            self.stu_grades.append(int(input("Enter the grade: ")))
    def display_graphs(self):
        plt.xlabel("Student Number")
        plt.ylabel("Grade")
        obj1 = course_grades()
        obj1.get_values()
        obj2 = course_grades()
        obj2.get_values()
        obj3 = course_grades()
        obj3.get_values()
        obj4 = course_grades()
        obj4.get_values()
        f=open('grades_info.dat', 'ab')
        pickle.dump(obj1, f)
        pickle.dump(obj2,f)
        pickle.dump(obj3, f)
        pickle.dump(obj4,f)
        f.close()
        f=open('grades_info.dat', 'rb')
        figure, axis = plt.subplots(2,2)
        axis[0,0].plot(obj1.stu_ID, obj1.stu_grades)
        axis[0,1].plot(obj2.stu_ID, obj2.stu_grades)
        axis[1,0].plot(obj3.stu_ID, obj3.stu_grades)
        axis[1,1].plot(obj4.stu_ID, obj4.stu_grades)
        plt.show()
        f.close()

while 1:
    x = course_grades()
    x.get_values()
    x.display_graphs()
