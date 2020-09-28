#De-queue
class Dequeue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

d=Dequeue()   
while True:
    print("\n1 Adding to right\n2 Adding to left\n3 Deleting from right\n4 Deleting from left\n5 Exit\n")
    c=int(input("Enter your choice : "))
    if c==1:
        print("Adding to the right: ") # Append to the right
        item=eval(input())
        d.addFront(item)
        print(d.items)
    elif c==2:
        print("Adding to the left: ") # Append to the left
        item=eval(input())
        d.addRear(item)
        print(d.items)
    elif c==3:
        print("Removing from the right: ") # Remove from the right
        if d.isEmpty():
            print('Underflow')
        else:
            d.removeFront()
            print(d.items)
    elif c==4:
        print("Removing from the left: ") # Remove from the left
        if d.isEmpty():
            print('Underflow')
        else:
            d.removeRear()
            print(d.items)
    elif c==5:
        exit()
    else:
        print("Please enter a valid input")
else:
    print("Please enter a valid input")

