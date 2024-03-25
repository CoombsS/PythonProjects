userNameC = ""
userPassC = ""
bkList = []


userList = {
    "user1": {"username": "colonh", "password": "admin1", "bookList": []},
    "user2": {"username": "coombss", "password": "admin2", "bookList": []},
}
books = {
    "book1": {"Title": "The Hobbit", "Author": "Tolkein", "Genre": "Fantasy", "Stock": 3},
    "book2": {"Title": "War of the Worlds", "Author": "Wells", "Genre": "Science Fiction", "Stock": 1},
    "book3": {"Title": "Fellowship of the Ring", "Author": "Tolkein", "Genre": "Fantasy", "Stock": 2},
    "book4": {"Title": "Good Omens", "Author": "Neil Gaiman", "Genre": "Comedy", "Stock": 3},
    "book5": {"Title": "Dante's Inferno", "Author": "Dante Alighieri", "Genre": "Epic", "Stock": 3},
    "book6": {"Title": "The Lion, the Witch and the Wardrobe", "Author": "C.S. Lewis", "Genre": "Fantasy", "Stock": 3},
    "book7": {"Title": "The Picture of Dorian Gray", "Author": "Oscar Wilde", "Genre": "Fiction", "Stock": 3},
    "book8": {"Title": "Sherlock Holmes and the Case of the Green Dragon", "Author": "Miguel Rivera",
              "Genre": "Fiction", "Stock": 3},
    "book9": {"Title": "Adventures of Huckleberry Finn", "Author": "Mark Twain", "Genre": "Fiction", "Stock": 3}
}


class users:
    def __init__(self, username, password, bookList):
        self.username = ""
        self.password = ""
        self.bookList = []

    def createNewUser(self):
        self.username = str(input("Please enter the username"))
        self.password = str(input("Please enter the password"))
        self.bookList = []

    def displayUserInfo(self):
        print(self.username)
        print(self.password)
        print(self.bookList)

    def checkOut(self):
        co = input("Enter the title of the book you wish to check out: ")
        for d in books.values():
            if d["Title"] == co:
                d["Stock"] -= 1
                self.bookList.append(co)
                print("Your checked out books are: ",self.bookList)
                return self.searchMain()



    def bookReturns(self):
        if len(self.bookList) > 0:
            print("Your checked out books are: ", self.bookList)
        elif len(self.bookList) == 0:
            print("You have no books checked out, you have nothing to return.")
            if __name__ == '__main__':
                return self.mainMenu()
        rTurn = input("Please enter the book you wish to return: ")
        if rTurn in self.bookList:
            for book in books.values():
                if book['Title'] == rTurn:
                    book['Stock'] += 1
                    self.bookList.remove(rTurn)
                    print("Your checked out books are:", self.bookList)
                    self.mainMenu()

        else:
            print("You do not have this book checked out, please enter a book you have checked out.")
            self.bookReturns()

    def displayBooksRented(self):
        if len(self.bookList) > 0:
            print("Your rented books are:", self.bookList)
        elif len(self.bookList) == 0:
            print("You have no books checked out")
        return self.mainMenu()
    def mainMenu(self):
        print("1. Search for a book")
        print("2. Return a book")
        print("3. Display rented books")
        print("4. Exit")
        ans = int(input("Enter your decision > "))
        if ans == 1:
            self.searchMain()
        if ans == 2:
            self.bookReturns()
        if ans == 3:
            self.displayBooksRented()
        if ans == 4:
            return 0

    def searchMain(self):
        print("-" * 10, "Search in stock", "-" * 10)
        print("1: Search by author")
        print("2: Search by title")
        print("3: Search by genre")
        print("4: Print entire catalogue (in stock, and out)")
        print("5. Checkout a book")
        print("6. Return to main menu")
        ans = int(input("Enter your decision: "))
        if ans == 1:
            self.searchAuthor()
        if ans == 2:
            self.searchTitle()
        if ans == 3:
            self.searchGenre()
        if ans == 4:
            self.searchAll()
        if ans == 5:
            self.checkOut()
        if ans == 6:
            self.mainMenu()

    def searchAll(self):
        for d in books.items():
            print(d)
        return self.searchMain()

    def searchGenre(self):
        sg = str(input("What is the genre you would like to search by?: "))
        for d in books.values():
            if d['Genre'] == sg and d['Stock'] >= 1:
                print(d)
        return self.searchMain()


    def searchTitle(self):
        st = str(input("What is the title you would like to search for?: "))
        for d in books.values():
            if d['Title'] == st and d['Stock'] >= 1:
                print(d)

        return self.searchMain()


    def searchAuthor(self):
        sa = str(input("What is the author's last name?: "))
        for d in books.values():
            if d['Author'] == sa and d['Stock'] >= 1:
                print(d)
        return self.searchMain()



def login():
    print("-" * 10, "Log into your account", "-" * 10)
    un = str(input("Enter your username: "))
    pw = str(input("Enter your password: "))
    for user in userList.values():
        if user['username'] == un and user['password'] == pw:
            userNameC = un
            userPassC = pw
            bkList = user['bookList'].copy()
            u1 = users(un,pw,bkList)
            u1.mainMenu()
            print("Login successful")
        elif user['username'] != un or user['password'] != pw:
            print("Sorry, your username and/or password was incorrect, please try again.")
        else:
            break

while 1:
    login()
