# Circular linked list traversal 

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=None
    def push(self,data):
        n=Node(data)
        temp=self.head
        n.next=self.head
        # If linked list is not None then set the next of
        # last node
        if self.head is not None:
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=n
        else:
            n.next=n
        self.head=n
    def printList(self):
        temp=self.head
        if self.head is not None:
            while(True):
                print(temp.data,"")
                temp=temp.next
                if (temp==self.head):
                    break
                
cllist = CircularLinkedList() 

# Created linked list will be 11->2->56->12 
cllist.push(4) 
cllist.push(3) 
cllist.push(2) 
cllist.push(1) 

print("Contents of circular Linked List: ")
cllist.printList() 
			
# This code is contributed by 
# Nikhil Kumar Singh(nickzuck_007) 
