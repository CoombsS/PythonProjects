from pymongo import MongoClient
import random

def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017"
    client = MongoClient(CONNECTION_STRING)
    return client['libraryusers']
dbname = get_database()

collection_name = dbname['user_details']

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
    def __init__(self):
        self.username = ''
        self.password = ''
        self.bookList = []

    def login(self):
        print('-'*10, "Login to your account", '-'*10)
        un = str(input("Enter your username: "))
        pw = str(input('Enter your password: '))
        flag = False

        usercheck = collection_name.find({'username': un})
        passcheck = collection_name.find({'password': pw})

        for un in usercheck:
            for pw in passcheck:
                flag = True

        if flag == True:
            print("login successful!")
            print()
            self.mainMenu()
        elif flag == False:
            print("login unsuccessful")
            print()
            response = input("Would you like to try again or create a new account? (y/n): ")
            if response == "y":
                users.login()
            elif response == 'n':
                temp = users()
                temp.createNewUser()
    def createNewUser(self):

        un = str(input("Enter your username: "))
        pw = str(input('Enter your password: '))

        log = {
            "username": un,
            "password": pw,
            "bookList": []
        }
        collection_name.insert_one(log)


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
        print("4. Request a new book")
        print("5. Exit")
        ans = int(input("Enter your decision > "))
        if ans == 1:
            self.searchMain()
        if ans == 2:
            self.bookReturns()
        if ans == 3:
            self.displayBooksRented()
        if ans == 4:
            count = 9
            self.requestBook()
        if ans == 5:
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

    def requestBook(self):
        print("Enter the information for your requested book:")
        title = input("Title: ")
        author = input("Author: ")
        genre = input("Genre: ")
        x = random.randint(0,100)

        books['book'+str(x)] = {"Title": title, 'Author': author, "Genre": genre, "Stock": 3}
        print(title, "has been added.")
        return self.mainMain()
while 1:
    action = users()
    x = action.login()
