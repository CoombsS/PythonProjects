from pymongo import MongoClient
def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017"
    client = MongoClient(CONNECTION_STRING)
    return client ['Bank']
dbname = get_database()
collection_name = dbname["Bank_customer"]
class Bank_customer:
    def __init__(self):
        self.acc_no = ""
        self.name = ""
        self.type = ""
        self.balance = ""
        self.address = ""
    def createCustomer(self):
        self.acc_no = input("Please enter the acc_no: ")
        self.name = input("Please enter the account name: ")
        self.type = input("Please enter the account type: ")
        self.balance = input("Please enter the balance amount: ")
        self.address = input("Please enter the address: ")
        account = {
            "acc_no" : self.acc_no,
            "name": self.name,
            "type": self.type,
            "balance":self.balance,
            "address":self.address,
        }
        collection_name.insert_one(account)
        exit()
while 1:
    u1 = Bank_customer()
    u1.createCustomer()