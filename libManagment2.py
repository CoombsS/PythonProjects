#TODO alot... not really actually its going well
#TODO returns
#TODO seperate file with usernames and pass: so users can create accounts and to check it to login
#TODO return book not checked out
#TODO fix booklist being reset when ran

userNameC = ""
userPassC = ""
bkList=[]


userList = {
    "user1": {"username": "colonh", "password": "admin1", "bookList":['War of the Worlds','The Hobbit']},
    "user2": {"username": "coombss", "password": "admin2", "bookList":[]},
}
books = {
    "book1": {"Title": "The Hobbit", "Author": "Tolkein", "Genre": "Fantasy", "Stock": 3},
    "book2": {"Title": "War of the Worlds", "Author": "Wells", "Genre": "Science Fiction", "Stock": 1},
    "book3": {"Title": "Fellowship of the Ring", "Author": "Tolkein", "Genre": "Fantasy", "Stock": 2},
    "book4": {"Title": "Good Omens", "Author": "Neil Gaiman", "Genre": "Comedy", "Stock": 3},
    "book5": {"Title": "Dante's Inferno", "Author": "Dante Alighieri", "Genre": "Epic", "Stock": 3},
    "book6": {"Title": "The Lion, the Witch and the Wardrobe", "Author": "C.S. Lewis", "Genre": "Fantasy","Stock": 3},
    "book7": {"Title": "The Picture of Dorian Gray", "Author": "Oscar Wilde", "Genre": "Fiction", "Stock": 3},
    "book8": {"Title": "Sherlock Holmes and the Case of the Green Dragon", "Author": "Miguel Rivera","Genre": "Fiction", "Stock": 3},
    "book9": {"Title": "Adventures of Huckleberry Finn", "Author": "Mark Twain", "Genre": "Fiction", "Stock": 3}
}




class user:
    def __init__(self,username,password,bookList):
        self.username = ""
        self.password = ""
        self.bookList = []
    def createNewUser(self, username, password):
        self.username = str(input("Please enter the username"))
        self.password = str(input("Please enter the password"))
        self.bookList = []
    def displayUserInfo(self,username,password,bookList):
        print(self.username)
        print(self.password)
        print(self.bookList)
    def checkOut(self,username,password,bookList):
        co = input("Enter the title of the book you wish to check out: ")
        for d in books.values():
            if d["Title"] == co:
                d["Stock"] -= 1
                self.bookList.append(co)
                print(self.bookList)
                print("Checkout sucessful!")
        return searchMain()

    def returns(self, username, password, bkList):        #CHANGE ALL booklist to BKLIST
        rTurn = str(input("Please enter the book you wish to return: "))
        if rTurn in bkList:
            for book in books.values():
                if book['Title'] == rTurn:
                    book['Stock'] += 1
                    bkList.remove(rTurn)
                else:
                    print("We do not carry this book.")
        else:
            print("You do not have this book checked out")
    def displayBooksRented(self, bookList):
        for book in self.bookList:
            print(book)

def searchAll():
    for d in books.items():
        print(d)
    return searchMain()
def searchGenre():
    sg = str(input("What is the genre you would like to search by?: "))
    for d in books.values():
        if d['Genre'] == sg and d['Stock'] >= 1:
            print(d)
    return searchMain()
def searchTitle():
    st = str(input("What is the title you would like to search for?: "))
    for d in books.values():
        if d['Title'] == st and d['Stock'] >= 1:
            print(d)
        else:
            print("Not found... checking next shelf...")
    return searchMain()
def searchAuthor():
    sa = str(input("What is the author's last name?: "))
    for d in books.values():
        if d['Author'] == sa and d['Stock'] >= 1:
            print(d)
        else:
            print("Not found, checking next shelf...")
    return searchMain()
def searchMain():
    print("-"*10,"Search in stock","-"*10)
    print("1: Search by author")
    print("2: Search by title")
    print("3: Search by genre")
    print("4: Print entire catalogue (in stock, and out)")
    print("5. Return to main menu")
    print("6. Checkout a book")
    ans = int(input("Enter your decision: "))
    if ans == 1:
        searchAuthor()
    if ans == 2:
        searchTitle()
    if ans == 3:
        searchGenre()
    if ans == 4:
        searchAll()
    if ans == 5:
        mainMenu()
    if ans == 6:
        u1 = user(userNameC,userPassC,[])
        u1.checkOut(userNameC,userPassC,[])


def login():
    print("-" * 10, "Log into your account", "-" * 10)
    un = str(input("Enter your username: "))
    pw = str(input("Enter your password: "))
    for x in userList.values():
        if x['username'] == un and x['password'] == pw:
            print("Login successful")
            mainMenu(un, pw, x['bookList'])
            userNameC = un
            userPassC = pw
            bkList=x['bookList'].copy()
            break
        else:
            continue




def mainMenu(un, pw, bk):
    print (un, pw, bk)
    print("1. Search for a book")
    print("2. Return a book")
    print("3. Display rented books")
    print("4. Exit")
    ans = int(input("Enter your decision > "))
    if ans == 1:
        searchMain()
    if ans == 2:
        print(un, pw, bk)
        u1 = user(un, pw, bk)
        u1.returns(un, pw, bk)
    if ans == 3:
        print(bk)
        mainMenu(un, pw, bk)




while 1:
    login()

