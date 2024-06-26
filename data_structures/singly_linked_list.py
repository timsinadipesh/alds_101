"""
Singly linked list

It can append data at the end of the list, prepend data, 
insert at a certain index and remove at a certain index
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, index, data):
        new_node = Node(data)
        curr_node = self.head
        if index == 0:
            new_node.next = curr_node
            self.head = new_node
            return

        for _ in range(index-1):
            if not curr_node:
                print(f"Node does not exist at index {index}.")
                return
            curr_node = curr_node.next

        new_node.next = curr_node.next
        curr_node.next = new_node

    def remove_after(self, index):
        curr_node = self.head
        for _ in range(index):
            if not curr_node:
                print(f"Node does not exist at index {index}.")
                return
            curr_node = curr_node.next
        next_node = curr_node.next
        curr_node.next = next_node.next

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()


# usage
linked_list = LinkedList()
linked_list.append("alpha")
linked_list.append("beta")
linked_list.append("theta")
linked_list.print_list()

linked_list.prepend("0")
linked_list.print_list()

linked_list.prepend("-beta")
linked_list.print_list()

linked_list.insert(1, "-alpha")
linked_list.print_list()

linked_list.remove_after(3)
linked_list.print_list()