#Queue
def insert(q,item):
    q.append(item)
def delete(q):
    if len(q)==0:
        return(-1)
    else:
        return(q.pop(0))    
q=[]
while True:
    print("\n1 Insert\n2 Delete\n3 Exit\n")
    c=int(input("Enter your choice : "))
    if c==1:
        item=int(input("Enter the item : "))
        insert(q,item)
        print(q)
    elif c==2:
        x=delete(q)
        if x==-1:
            print("Underflow")
        else:
            print("\nPopped item : ",x)
    elif c==3:
        exit()
    else:
        print("Please enter a valid input")
else:
    print("Please enter a valid input")
