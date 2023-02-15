class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = None
        self.tail = None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end="->")
            temp = temp.next
        print("None")

    def append_tail(self, value):
        tail_node = Node(value)
        if self.head is None:
            self.head = tail_node
            self.tail = self.head
            return

        self.tail.next = tail_node
        self.tail = tail_node
        
    def prepend(self, value):
        n_node = Node(value)
        n_node.next = self.head
        self.head = n_node
        if self.head.next is None:
            self.tail = self.head

    # new_node = Node(7)


# new_linkedlist = LinkedList()
# print(new_node.value)
# print(new_linkedlist.head)

lst = LinkedList()
lst.prepend(9)
# lst.prepend(5)
# lst.prepend(6)
lst.print_list()
lst.append_tail(9)
# lst.append_tail(5)
# lst.append_tail(4)
# print(lst.head.value)
print(lst.tail.value)
