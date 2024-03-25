class Queue:
    def __init__(self):
        self.title = ""
        self.Q = []
    def createQ(self):
        self.title = input("Enter the title of the Queue:")
        self.Q = []
        print(self.title, self.Q)
    def addToQ(self):
        a = input("Enter the title of the queue you would like to add to:")
        b = input("Enter the value to insert")
        a.append(b)
    def pop(self):
        self.Q.pop()
        print(self.Q)
    def displayQ(self):
        print(self.title)
        print(self.Q)

qcount = 1
while 1:
    print("1. Create a new  empty queue")
    print("2. Add item to a queue")
    print("3. Delete item from a queue")
    print("4. Display the queues")
    print("5. Create a new empty stack")
    print("6. Add item to a stack")
    print("7. Delete an item from a stack")
    print("8. Display the stacks")
    print("9. Quit")
    ans = input("Enter your answer:")
    if ans == 1:
        Queue.createQ()
    if ans == 2:
        Queue.addToQ()

