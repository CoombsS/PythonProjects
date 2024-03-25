class Account_holder:
    def __init__(self,w,x,y,z):
        self.name = w
        self.acc_no = x
        self.bal = int(y)
        self.type = z
    def transfer(self,obj):
        xa = int(input("Enter the amount to transfer:"))
        if xa > self.bal:
            print("Insufficient funds")
        elif xa < self.bal:
            self.bal -= xa
            obj.bal += xa
            print("Transfer sucessful")
    def withdrawl(self):
        xb = int(input("Enter the amount you would like to withdraw: "))
        if xb > self.bal:
            print("Insufficient funds")
        else:
            self.bal -= xb
            print("Withdraw successful")
    def deposit(self):
        xd = int(input("Enter the amount you wish to deposit: "))
        self.bal += xd
    def display_Bal(self):
        print(self.name, "'s balance is:", self.bal)