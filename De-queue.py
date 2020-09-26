#De-queue
import collections
# Create a de-queue
de_q=collections.deque()

while True:
    print("\n1 Adding to right\n2 Adding to left\n3 Deleting from right\n4 Deleting from left\n5 Exit\n")
    c=int(input("Enter your choice : "))
    if c==1:
        print("Adding to the right: ") # Append to the right
        item=eval(input())
        de_q.append(item)
        print(de_q)
    elif c==2:
        print("Adding to the left: ") # Append to the left
        item=eval(input())
        de_q.appendleft(item)
        print(de_q)
    elif c==3:
        print("Removing from the right: ") # Remove from the right
        de_q.pop()
        print(de_q)
    elif c==4:
        print("Removing from the left: ") # Remove from the left
        de_q.popleft()
        print(de_q)
    elif c==5:
        exit()
    else:
        print("Please enter a valid input")
else:
    print("Please enter a valid input")

