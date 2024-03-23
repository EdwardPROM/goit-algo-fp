class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.insert_into_sorted_list(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def insert_into_sorted_list(self, head, new_node):
        if not head or new_node.data <= head.data:
            new_node.next = head
            return new_node
        prev = head
        current = head.next
        while current and current.data < new_node.data:
            prev = current
            current = current.next
        new_node.next = current
        prev.next = new_node
        return head

    def merge_sorted_lists(self, other):
        dummy = Node()
        tail = dummy
        current1 = self.head
        current2 = other.head
        while current1 and current2:
            if current1.data < current2.data:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            tail = tail.next
        if current1:
            tail.next = current1
        if current2:
            tail.next = current2
        self.head = dummy.next


# Приклад використання

llist1 = LinkedList()
llist1.insert_at_beginning(5)
llist1.insert_at_beginning(10)
llist1.insert_at_beginning(15)

llist2 = LinkedList()
llist2.insert_at_beginning(20)
llist2.insert_at_beginning(25)
llist2.insert_at_beginning(30)

print("Зв'язний список 1:")
llist1.print_list()
llist1.reverse_list()
print("Зв'язний список 1 після реверсу:")
llist1.print_list()
llist1.insertion_sort()
print("Відсортований зв'язний список 1:")
llist1.print_list()
print("Зв'язний список 2:")
llist2.print_list()
llist2.insertion_sort()
print("Відсортований зв'язний список 2:")
llist2.print_list()
llist1.merge_sorted_lists(llist2)
print("Відсортовані списки 1 і 2 об'єднані в один відсортований список:")
llist1.print_list()

