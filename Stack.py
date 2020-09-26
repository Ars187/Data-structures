#Stack
def push(stack,item):
    stack.append(item)
def pops(s):
    if len(stack)==0:
        return(-1)
    else:
        return(stack.pop())    
stack=[]
while True:
    print("\n1 Push\n2 Pop\n3 Exit\n")
    c=int(input("Enter your choice : "))
    if c==1:
        item=int(input("Enter the item : "))
        push(stack,item)
        print(stack)
    elif c==2:
        x=pops(stack)
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
