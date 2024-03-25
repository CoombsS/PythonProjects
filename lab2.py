myStudents = {
}
while 1:
    print("1. Add a student")
    print("2. Delete a student")
    print("3. Modify a student")
    print("4. Display all students")
    print("5. Exit")
    ans = int(input("What is your decision?: "))
    if ans == 1:
        sname = input("Please enter the student's name: ")
        LG1 = int(input("Please enter the grade for Lab1:"))
        LG2 = int(input("Please enter the grade for Lab2:"))
        LG3 = int(input("Please enter the grade for Lab3:"))
        LG4 = int(input("Please enter the grade for Lab4:"))
        LG5 = int(input("Please enter the grade for Lab5:"))
        i = len(myStudents)
        i = i + 1
        tp = LG1 + LG2 +LG3 +LG4 +LG5
        per = (LG1 + LG2 +LG3 +LG4 +LG5)/5
        avg = ((LG1 + LG2 + LG3 + LG4 + LG5)/5)*10
        myStudents["student" + str(i)] = {"name":sname,"TotalPoints":tp,"Percent":per,"Average":avg, "Lab1":LG1,"Lab2":LG2,"Lab3":LG3,"Lab4":LG4,"Lab5":LG5}
    if ans == 2:
        ds = str(input("Please enter the student you would like to remove (ex:student1, student2. ect.): "))
        del myStudents[ds]
    if ans == 3:
        ms = input("Please enter the student you would like to modify: ")
        mg = input("Please enter the grade you would like to modify: ")
        eg = int(input("Please enter the student's new grade: "))
        myStudents[ms][mg] = eg
    if ans == 4:
        print(str(myStudents))
    if ans == 5:
        break