usersL = {
    "user1": {"username": "colonh", "password": "admin1", "bookList":[]},
    "user2": {"username": "coombss", "password": "admin2", "bookList":[]},
}

class users:
    def __init__(self):
        self.name = ""
        self.password = ""
        self.books = []
    def createNewUser(self):
        self.name = input("Please enter the name of the new user: ")
        self.password = input("Please enter the password of the user ")
        self.books = []
    def checkOut(self):
        userN = input("Enter your username: ")
        chkout = input("Enter the title of the book you wish to checkout: ")
        for d in books.values():
            if d["Title"] == chkout:
                d["Stock"] -= 1
                print(d)                                                                    ##FIX THIS
                self.books.append(chkout)
    def login(self):
        print("-" * 10, "Log into your account", "-" * 10)
        un = str(input("Enter your username: "))
        pw = str(input("Enter your password: "))
        for x in usersL.values():
            if x['username'] == un and x['password'] == pw:
                print("login successful!")
                searchMain()
                break
            elif x['username'] != un or x['password'] != pw:
                print("Login unsucessful")
                return users.login(u1)


def searchAll():
    for d in books.items():
        print(d)

def searchGenre():
    sg = str(input("What is the genre you would like to search by?: "))
    for d in books.values():
        if d['Genre'] == sg and d['Stock'] >= 1:
            print(d)

def searchTitle():
    st = str(input("What is the title you would like to search for?: "))
    for d in books.values():
        if d['Title'] == st and d['Stock'] >= 1:
            print(d)
        else:
            print("Not found... checking next shelf...")

def searchAuthor():
    sa = str(input("What is the author's last name?: "))
    for d in books.values():
        if d['Author'] == sa:
            print(d)
        else:
            continue
    chko = input("Would you like to check out a book? (y/n): ")
    if chko == 'y' or 'Y':
        return users().checkOut()
    elif chko == 'n' or 'N':
        return searchMain()

def searchMain():
    print("-"*10,"Search in stock","-"*10)
    print("1: Search by author")
    print("2: Search by title")
    print("3: Search by genre")
    print("4: Print entire catalogue (in stock, and out)")
    ans = int(input("Enter your decision: "))
    if ans == 1:
        searchAuthor()
    if ans == 2:
        searchTitle()
    if ans == 3:
        searchGenre()
    if ans == 4:
        searchAll()

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

while 1:
    u1 = users()
    users.login(u1)