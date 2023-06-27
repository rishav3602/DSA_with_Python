## Inserting a node at the end of the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    ## insert at the end of the linked list
    def insert_at_End(self, new_data):
        ## creation of the new node
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        ## insertion at the end
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node


    ## deletion of a node
    def Del_node(self,pos):
        ## check if linked list is empty or not
        if self.head is None:
            return
        
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
            if temp is None:
                return
            
        next_ptr = temp.next.next
        temp.next = None
        temp.next = next_ptr



    ## print the linked list
    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.data)+" ",end=" ")
            temp = temp.next



llist = LinkedList()
llist.insert_at_End(1)
llist.insert_at_End(2)
llist.insert_at_End(3)
llist.insert_at_End(4)
llist.insert_at_End(5)
llist.insert_at_End(6)
llist.printList()
llist.Del_node(3)
print()
llist.printList()