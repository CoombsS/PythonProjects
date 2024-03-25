class Book_class:
    def __init__(self):
        bookID = ""
        bookTitle = ""
        authorID = ""
        publisher = ""
        edition = ""
        yearOfPub = ""
    def create_a_book(self):
        self.bookID = input("Please enter the bookID: ")
        self.bookTitle = input("Please enter the book title: ")
        self.authorID = input("Please enter the author ID: ")
        self.publisher = input("Please enter the publisher: ")
        self.edition = input("Please enter the edition number: ")
        self.yearOfPub = input("Please enter the year of publication: ")
    def display_book(self):
        return f"ID:{self.bookID} \nTitle: {self.bookTitle} \nAuthor:{self.authorID}"
    def __str__(self):
        for i in range(1,Bcount):
            print(mybook)
class Author_class:
    def __init__(self):
        authorID = ""
        authorName = ""
        affiliation = ""
        country = ""
        phone = ""
        emailID = ""
    def create_author(self):
        self.authorID = input("Please enter the author's ID: ")
        self.authorName = input("Please enter the author's name: ")
        self.affiliation = input("Please enter the author's affiliation: ")
        self.country = input("Please enter the author's country: ")
        self.phone = input("Please enter the author's phone number: ")
        self.emailID = input("Please enter the author's phone number: ")
    def display_author(self):
        print(self.authorID)
        print(self.authorName)
        print(self.affiliation)
        print(self.country)
        print(self.phone)
        print(self.emailID)
class User_class:
    def __init__(self):
        userID = ""
        userName = ""
        userPass = ""
        address = ""
        emailID = ""
        phone = ""
    def create_user(self):
        self.userID = input("Please enter the userID: ")
        self.userName = input("Please enter the user name: ")
        self.userPass = input("Please enter the user password: ")
        self.address = input("Please enter the user's address: ")
        self.emailID = input("Please enter the emailID: ")
        self.phone = input("Please enter the phone number: ")
    def display_user(self):
        print(self.userID)
        print(self.userName)
        print(self.userPass)
        print(self.address)
        print(self.emailID)
        print(self.phone)
class Lending_Books_class:
    def __init__(self):
        lendingID = ""
        bookID = ""
        userID = ""
        dateLen = ""
        dateRet = ""
    def create_a_lend(self):
        self.lendingID = input("Please enter the ID of the lend: ")
        self.bookID = input("Please enter the ID of the book: ")
        self.userID = input("Please enter the user ID: ")
        self.dateLen = input("Please enter the date the lend started: ")
        self.dateRet = input("Please enter the date the lend was returned: ")
    def display_lend(self):
        print(self.lendingID)
        print(self.bookID)
        print(self.userID)
        print(self.dateLen)
        print(self.dateRet)
bookList = {}
authorList = {}
userList = {}
lendList={}
while 1:
    Bcount = 1
    Ucount = 1
    Acount = 1
    Lcount = 1
    print("1. Enter a new book")
    print("2. Add a new user")
    print("3. Add a new author")
    print("4. Create a new lend")
    print("5. Display all books")
    print("6. Display all users")
    print("7. Display all authors")
    print("8. Display all the books currently on lend")
    print("9. Exit")
    ans = int(input("What is your decision?: "))
    if ans == 1:
        mybook = "book" + str(Bcount)
        mybook=Book_class()
        mybook.create_a_book()
        mybook.display_book()
        Bcount = Bcount +1
    if ans == 2:
        Nuser = "user" +str(Ucount)
        Nuser = User_class()
        Nuser.create_user()
        Nuser.display_user()
        Ucount = Ucount +1
    if ans == 3:
        Nauthor = "author" +str(Acount)
        Nauthor = Author_class()
        Nauthor.create_author()
        Nauthor.display_author()
        Acount = Acount +1
    if ans == 4:
        Nlend = "lend" +str(Lcount)
        Nlend = Lending_Books_class()
        Nlend.create_a_lend()
        Nlend.display_lend()
        Lcount = Lcount +1
    if ans == 5:
        for i in range(1, Bcount):
            mybook = "book" + i
            mybook.display_book()
    if ans == 6:
        for i in range(0, Ucount):
            Nuser = "user" + i
            Nuser.display_user()



