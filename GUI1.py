import matplotlib.pyplot as plt
import numpy as np

x = np.array([2011,2012,2013,2014,2015,2016])
y= np.array([12,52,13,63,24,75])

figure, axis = plt.subplot(2,2)
axis[0,0].plot(x,y)

a = [2011,2012,2013,2014,2015]
b = [21,19,24,17]

plt.plot(x,y)
plt.show()

plt.scatter(x,y)
plt.show(x,y)



x = [1,2,3,4,5,6,7,8,9,10]
class course:
    def __init__(self):
        self.cName = ""
        self.grades = []
    def displayGraph(self):
        plt.plot(x, self.grades)
        plt.scatter(x,self.grades)
        plt.show()
    def getInfo(self):
        self.cName = input("Enter the course name: ")
        for i in range(1,11):
            self.grades = int(input("Enter the grade: "))

while 1:
    c1 = course()
    c1.getInfo()
    c1.displayGraph()