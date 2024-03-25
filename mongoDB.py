from pymongo import MongoClient
import pymongo

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://localhost:27017"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    #from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['University']


# This is added so that many files can reuse the function get_database()

dbname = get_database()
print("Database Details:", dbname)

collection_name = dbname["Students"]


stu_1 = {
"stu_id" : "222",
"stu_name" : "Justus",
"dept" : "CS",
"course" : "DB",
}

stu_2 = {
"stu_id" : "789",
"stu_name" : "Blender",
"dept" : "CS",
"course" : "OOP",
}
stu_3 = {
"stu_id" : "369",
"stu_name" : "Justus",
"dept" : "CS",
"course" : "OOP",
}

mylist = [stu_1, stu_2, stu_3]
# collection_name.insert_one(stu_2)
collection_name.insert_many(mylist)