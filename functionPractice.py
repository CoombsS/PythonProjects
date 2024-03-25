while 1:
    def sqArea():
        w = int(input("Enter width"))
        l = int(input("Enter length"))
        area = w * l
        return area
    def sqVol():
        w = int(input("Enter width"))
        l = int(input("Enter length"))
        h = int(input("Enter the height"))
        vol = w * l * h
        return vol
    def circ():
        r = int(input("Enter the radius"))
        c = 3.1459 * r
        return c
    def cArea():
        r = int(input("Enter the radius"))
        cA = (3.1459 * r) ** 2
        return cA
    def cylArea():
        r = int(input("Enter the radius"))
        h = int(input("Enter the height"))
        cyA = (2 * 3.1459 * h) + (2 * 3.1459 * r) ** 2
        return cyA
    print("1. Calculate area of square.")
    print("2. Calculate volume of square.")
    print("3. Calculate circumference.")
    print("4. Calculate area of circle.")
    print("5. Calculate volume of cylinder.")
    print("6. Quit.")
    ans = int(input("Enter your decision: "))
    if ans == 1:
        print(sqArea())
    if ans == 2:
        print(sqVol())
    if ans == 3:
        print(circ())
    if ans == 4:
        print(cArea())
    if ans == 5:
        print(cylArea())
    if ans == 6:
        break

