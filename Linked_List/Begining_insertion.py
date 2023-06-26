## Inserting a node at the begining of the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    ## insert at the front/beginning of the linked list
    def insertAtBeginning(self, new_data):
        ## creation of the new node
        new_node = Node(new_data)
        ## insertion at the beginning
        new_node.next = self.head
        self.head = new_node
    
    ## print the linked list
    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.data)+" ",end=" ")
            temp = temp.next


llist = LinkedList()
llist.insertAtBeginning(10)
llist.insertAtBeginning(9)
llist.insertAtBeginning(8)
llist.insertAtBeginning(7)
llist.printList()