#Queue
class queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def insert(self,value):
        self.items.append(value)
    def delete(self):
        return self.items.pop(0)   
q=Queue()
while True:
    print("\n1 Insert\n2 Delete\n3 Exit\n")
    c=int(input("Enter your choice : "))
    if c==1:
        value=int(input("Enter the item : "))
        q.insert(value)
        print(q.items)
    elif c==2:
        if q.is_empty():
            print("Underflow")
        else:
            print("\nPopped item : ",q.delete())
    elif c==3:
        exit()
    else:
        print("Please enter a valid input")
else:
    print("Please enter a valid input")
