#Create a dictionary with students and their details: name, major, minor, emphasis, and CGPA.

myStudents = {
    "student1" :{
        "Name":"Skyler",
        "Major": "CS",
        "Minor": "Bible",
        "Emphasis":"Cyber",
        "CGPA":"3.5"
    },
    "student2":{
        "Name":"Opal",
        "Major":"Marketing",
        "Minor":"Psychology",
        "Emphasis":"DigitalMarketing",
        "CGPA":"3.9"
    },
    "student3":{
        "Name":"Alex",
        "Major":"Mechanical Engineering",
        "Minor":"Electrical Engineering",
        "Emphasis":"None",
        "CGPA":"3.2"
    },
    "student4":{
        "Name":"Tyler",
        "Major":"CS",
        "Minor":"Robotics",
        "Emphasis":"ME",
        "CGPA":"3.7"
    }
}
i = 1
for x in myStudents:
    j=str(i)
    print(myStudents["Student"+j].values())

    if("CS" in myStudents["Student" + j]["minor"] and "ME" in myStudents["Student" + j]["emphasis"]):
        print(myStudents["Student" + j])
    i=i+1