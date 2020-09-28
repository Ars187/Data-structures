#Stack
class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
    
s=Stack()
while True:
    print("\n1 Push\n2 Pop\n3 Exit\n")
    c=int(input("Enter your choice : "))
    if c==1:
        data=int(input("Enter the item : "))
        s.push(data)
        print(s.items)
    elif c==2:
        if s.is_empty():
            print("Underflow")
        else:
            print("\nPopped item : ",s.pop())
    elif c==3:
        exit()
    else:
        print("Please enter a valid input")
else:
    print("Please enter a valid input")
