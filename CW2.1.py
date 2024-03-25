names = ['Skyler', 'Opal', 'Emily', 'Marc', 'Daisy', 'Stephen', 'Cathy', 'Ramona', 'Don', 'Landon']
ages = [24,19,46,50,9,78,76,75,79,23]
while 1:
    print("1. Add an element to the list.")
    print("2. Remove an element from the list.")
    print("3. Replace an element in the list.")
    print("4. Reverse the elements in the list.")
    print("5. Print the list elements.")
    print("6. Exit")
    ans = int(input("Please enter your choice: "))
    if ans == 1:
        names.append(str(input("Enter the new name:")))
        ages.append(int(input("Enter the new age:")))
    if ans == 2:
        index = names.index(input(str("Please enter the name to remove:")))
        names.pop(index)
        ages.pop(index)
    if ans == 3:
        rName = input("Enter the name you would like to replace: ")
        nName = input("Enter what you would like to replace " + rName + " with:")
        nAge = int(input("Enter " + nName + "'s age:"))
        index = names.index(rName)
        names[index] = nName
        ages[index] = nAge
    if ans == 4:
        names = list(names)
        names.reverse()
        ages.reverse()
    if ans == 5:
        print(names)
        print(ages)

