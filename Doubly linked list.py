# Doubly linked list

# Node 
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None

# Class for Doubly Linked List 
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        if self.head is not None:
            self.head.prev=new_node
            self.head=new_node
    def insertAfter(self,prev_node,new_data):
        # Check if the given prev_node is None
        if prev_node is None:
            print("The previous node is empty")
            return()
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
        new_node.prev=prev_node
        if new_node.next is not None:
            new_node.next.prev=new_node
    def append(self,new_data):
        new_node=Node(new_data)
        new_node.next=None
        # If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            new_node.prev=None
            self.head=new_node
            return()
        # Else traverse till the last node
        last=self.head
        while(last.next is not None):
            last=last.next
        last.next=new_node
        new_node.prev=last
        return()
    def printList(self,node):
        while(node is not None):
            print(node.data,"")
            node=node.next

llist=DoublyLinkedList()  
llist.append(4) 
llist.push(2) 
llist.push(1) 
llist.append(5) 
llist.insertAfter(llist.head.next,3) 

print("Created DLL is: ")
llist.printList(llist.head) 
