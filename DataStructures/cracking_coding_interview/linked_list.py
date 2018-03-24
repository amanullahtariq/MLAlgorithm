class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):

        new_node = Node()
        new_node.data = data

        if self.head == None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next =new_node

    def prepend(self,data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self,data):
        node = self.head
        if node == None:
            return

        if node.data == data:
            self.head = self.head.next

        while node.next != None:
            if node.next.data == data:
                node.next = node.next.next
                return
            node = node.next

    def traverse_all(self):
        node = self.head
        while node != None:
            print (node.data)
            node = node.next

#def append(self, data):

linked_list = LinkedList()
linked_list.append(6)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(4)
linked_list.delete_with_value(4)
linked_list.traverse_all()