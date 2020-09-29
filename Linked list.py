#Linked list 

#Node class 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 


#Linked List class 
class LinkedList: 
    def __init__(self): 
        self.head=None
    def printL(self):
        a=self.head
        while (a):
            print(a.data)
            a=a.next

llist=LinkedList() 
llist.head=Node('S')
second=Node('U') 
third=Node('C')
fourth=Node('C')
fifth=Node('E')
sixth=Node('S')
seventh=Node('S')

#Linking nodes
llist.head.next=second  
second.next=third 
third.next=fourth 
fourth.next=fifth
fifth.next=sixth
sixth.next=seventh
llist.printL() 
