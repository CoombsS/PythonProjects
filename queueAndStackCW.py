class Queue:
    def __init__(self):
        name = ""
        list = []
    def createQueue(self):
        self.name = input("Enter the title of the queue:")
        self.list = []
        print(self.name, self.list)
    def enqueue(self):
        a = input("Enter the title of the queue you would like to add to:")
        b = input("Enter the value to insert")
        a.append(b)
    def displayQ(self):
        print(self.name)
    def pop(self, index=-1):
        return list.name.pop(index)


qNum = 1
lNum = 1
Nqueue = 1
eleNum = 1

while 1:
    print("1. Create a new  empty queue")
    print("2. Add item to a queue")
    print("3. Delete item from a queue")
    print("4. Display all queues")
    print("5. Create a new empty stack")
    print("6. Add item to a stack")
    print("7. Delete an item from a stack")
    print("8. Display all stacks")
    print("9. Quit")
    ans = input("Please enter your decision:")
    if ans == 1:
        Nqueue = "queue" + str(qNum)
        Nqueue = Queue()
        Nqueue.createQueue()
        qNum = qNum +1
    if ans == 2:
        Nele = input("Please enter the element you would like to enter:")
        Nele = Queue()
        Nele.enqueue()
        eleNum = eleNum +1

