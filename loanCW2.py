while 1:
    user = str(input("Please enter the user:"))
    principal = int(input("Please enter the principal amount:"))
    R = int(input("Please enter the rate:"))
    rate = R/(12*100)
    duration = int(input("Please enter the duration of the loan:"))
    emi = principal*rate*((1+rate)**duration)/((1+rate)**duration-1)
    emi = round(emi,2)
    print("Monthly EMI is:", emi)
    loanTuple = (user , principal , rate , duration)
    emiTuple = ()

while 1:
    print("1. Add user to loan tuple")
    print("2. Print loan tuple")
    ans = int(input("What would you like to do?: "))
    if ans == 1:
        user = str(input("Please enter the user:"))
        principal = int(input("Please enter the principal amount:"))
        R = int(input("Please enter the rate:"))
        rate = R / (12 * 100)
        duration = int(input("Please enter the duration of the loan:"))
        emi = principal * rate * ((1 + rate) ** duration) / ((1 + rate) ** duration - 1)
        emi = round(emi, 2)
        print("Monthly EMI is:", emi)
        d = input("Continue?: ")
        if d == 'y':
