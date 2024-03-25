names = []
ages = []

while 1:
    print("1. Add an element to the list.")
    print("2. Remove an element from the list.")
    print("3. Replace an element in the list.")
    print("4. Reverse the elements in the list.")
    print("5. Print the list elements.")
    print("6. Exit")
    ans = int(input("Please enter your choice: "))
    if ans == 1:
        names.append(str(input("Please enter the name: ")))
        ages.append(input("Please enter the age: "))
    if ans == 2:
        index = names.index(input("Please enter the name you would like to remove: "))
        names.pop(index)
        ages.pop(index)
    if ans == 3:
        rName = input("Enter the name you would like to replace: ")
        nName = input("Enter what you would like to replace " + rName + " with:")
        nAge = int(input("Enter " + nName + "'s age:"))
        index = names.index(rName)
        names = str(names)
        names.replace(nName, rName)
    if ans == 4:
        names = list(names)
        names.reverse()
        ages.reverse()
    if ans == 5:
        print(names)
        print(ages)
