my_dictionary = {
  "one": 1,
  "two": 2
}
print("Before:", my_dictionary)
my_dictionary["one"] = 3
print("After:", my_dictionary)

myBooks = {
    "book1":{"Book_no":"CS152", "Title":"Python OOP", "Author":"Steven", "Edition":"3", "Publisher":"Pckt", "Year":"2019"},
    "book2":{"Book_no":"MS116", "Title":"Learn Guitar in 30 days", "Author":"Bob", "Edition":"1", "Publisher":"Gamma", "Year":"2010"}
}
a = input("enter:")
myBooks["book3"]={"Book_no":a}
print(myBooks)