myUsers = {
    "user1":{
        "userid":"justus",
        "password":"123"
    },
    "user2":{
        "userid":"jim",
        "password":"345"
    },
    "user3":{
        "userid":"john",
        "password":"678"
    },
    "user4":{
        "userid":"coby",
        "password":"901"
    }
}
while 1:
    uname = input("Please enter your username: ")
    pword = input("Please enter your password: ")
    for user in myUsers:
        if myUsers[str(user)]["userid"] == uname and myUsers[str(user)]["password"] == pword:
            flag="T"
        else:
            flag="F"
    if flag == "T":
        print("Valid user")
    elif flag == "F":
        print("Invalid user")