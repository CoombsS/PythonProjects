"""
#write file
file1 = open("test1.txt", "a")
file1.writelines("Hello, Skyler\n")
file1.close()
nr = 1
#read file
file1 = open("test1.txt","r")
for line in file1:
    print(line)
    file1.writelines("LineRead")
"""

books = {
    "book1" : {"Title": "The Hobbit","Author":"Tolkein","Genre":"Fantasy", "Stock":3},
    "book2" : {"Title": "War of the Worlds","Author":"Wells","Genre":"Science Fiction", "Stock":1},
    "book3" : {"Title": "Fellowship of the Ring", "Author":"Tolkein","Genre":"Fantasy","Stock":2},
    "book4" : {"Title": "Good Omens", "Author": "Neil Gaiman", "Genre": "Comedy", "Stock": 3},
    "book5" : {"Title": "Dante's Inferno", "Author": "Dante Alighieri", "Genre":"Epic", "Stock": 3},
    "book6" : {"Title": "The Lion, the Witch and the Wardrobe", "Author": "C.S. Lewis", "Genre": "Fantasy", "Stock": 3},
    "book7" : {"Title": "The Picture of Dorian Gray", "Author": "Oscar Wilde", "Genre": "Fiction", "Stock": 3},
    "book8" : {"Title": "Sherlock Holmes and the Case of the Green Dragon", "Author": "Miguel Rivera", "Genre": "Fiction", "Stock": 3},
    "book9" : {"Title": "Adventures of Huckleberry Finn", "Author": "Mark Twain", "Genre": "Fiction", "Stock": 3}
}

#copies dictionary to file
with open("test2.txt",'a') as f:
    for key, value in books.items():
        f.write('%s:%s\n' % (key,value))
#reads from a dictionary
with open("zz1.txt","r") as f:
    data = f.read()

print(data)