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
def searchAuthor():
    sa = str(input("What is the author's last name?: "))
    for d in books.values():
        if d['Author'] == sa:
            print(d)
    chko = input("Would you like to check out a book? (y/n): ")
    if chko == 'y' or 'Y':
        return checkOut()
    elif chko == 'n' or 'N':
        return searchMain()
def searchTitle():
    st = str(input("What is the title you would like to search for?: "))
    for d in books.values():
        if d['Title'] == st and d['Stock'] >= 1:
            print(d)
        else:
            print("Not found... checking next shelf...")

def searchGenre():
    sg = str(input("What is the genre you would like to search by?: "))
    for d in books.values():
        if d['Genre'] == sg and d['Stock'] >= 1:
            print(d)
def searchAll():
    for d in books.items():
        print(d)
def checkOut():
    chkout = input("Enter the number of the book you wish to check out: ")
    [chkout]['Stock'] = x
    x -= 1




books = {
    "book1" :{"Title":"The Hobbit","Author":"Tolkein","Genre":"Fantasy", "Stock":3},
    "book2":{"Title":"War of the Worlds","Author":"Wells","Genre":"Science Fiction", "Stock":1},
    "book3":{"Title":"Fellowship of the Ring", "Author":"Tolkein","Genre":"Fantasy","Stock":2}
}

while 1:
    searchMain()
