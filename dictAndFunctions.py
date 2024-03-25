#stack - push/pop
#queue - enqueue/dequeue (doing a q)
myBooks = {
    "book1":{"Book_no":"CS152", "Title":"Python OOP", "Author":"Steven", "Edition":"3", "Publisher":"Pckt", "Year":"2019"},
    "book2":{"Book_no":"MS116", "Title":"Learn Guitar in 30 days", "Author":"Bob", "Edition":"1", "Publisher":"Gamma", "Year":"2010"}
}
q = []
def enqueueABook():
    app = input("Enter the book number you would like to queue: ")
    q.append(myBooks[app])
    return q
def dequeueABook():
    q.pop(0)
    return q
#TODO modABook
def modABook():
    bn = input("Enter the book number you would like to modify: ")
    bf = input("Enter the field you would like to edit: ")
    nd = input("Enter the field's new data: ")
    myBooks[bn][bf] = nd
def search():
    s = str(input("What book number are you looking for?: "))
    if myBooks[s] in q:
        return "Found"
    else:
        return "Not Found"
while 1:
    print("1. Get details and queue a book. ")
    print("2. Remove a book from the queue. ")
    print("3. Modify a book's details. ")
    print("4. Search for a book's avalibility. ")
    print("5. Display all books in the queue. ")
    print("6. Quit")
    ans = int(input("Please enter your decision: "))
    if ans == 1:
        enqueueABook()
    if ans == 2:
        dequeueABook()
    if ans == 3:
        modABook()
    if ans == 4:
        print(search())
    if ans == 5:
        print(q)
    if ans == 6:
        break
