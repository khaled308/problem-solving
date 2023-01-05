class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node

        else:
            self.tail.next = node

        self.tail = node

    def pop(self):
        temp = self.head

        while temp.next is not self.tail:
            temp = temp.next

        n = self.tail
        temp.next = None
        self.tail = temp
        return n

    def print(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next


l = SinglyLinkedList()
l.push(10)
l.push(5)
l.pop()

l.print()
