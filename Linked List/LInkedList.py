class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("END")

    def delete(self, value):
        if self.head is None:
            return 
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

# creating an empty linked list
new_list = LinkedList()
# adding to the linked list
new_list.append(3)
new_list.append(39)
#Display Linked List
new_list.display()
#Delete from Linked List
new_list.delete(3)
new_list.display()