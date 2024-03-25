q = []
while 1:
    print("1. Add an element")
    print("2. Remove an element")
    print("3. Modify an element")
    print("4. Print")
    print("5. Quit")
    ans = int(input("What is your decision?: "))
    if ans == 1:
        app = input("What would you like to add?:")
        q.append(app)
    if ans == 2:
        a = len(q)
        if a == 0:
            print("Queue is empty")
        else:
            q.pop(0)
    if ans == 3:
        mod = input("Enter the element you would like to modify: ")
        modE = str(input("Enter the new value of the element: "))
        for i in range(0, len(q)):
            if q[i] == mod:
                q[i] = modE
    if ans == 4:
        print(q)
    if ans == 5:
        break

