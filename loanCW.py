emiL = []
loanL = []
while 1:
    print("1. Enter new user loan data.")
    print("2. Print the data")
    print("3. Exit")
    ans = int(input("What is your decision:"))
    if ans == 1:
        principal = int(input("Enter the principal amount:"))
        rate = int(input("Please enter the rate:"))
        duration = int(input("Please enter the duration:"))
        emi = principal * rate * ((1+rate)**duration)/((1+rate)**duration -1)
        loanL.append(principal)
        loanL.append(rate)
        loanL.append(duration)
        emiL.append(emi)
    if ans == 2:
        emiT = tuple(emiL)
        loanT = tuple(loanL)
        print(loanT)
        print(emiT)
    if ans == 3:
        break
