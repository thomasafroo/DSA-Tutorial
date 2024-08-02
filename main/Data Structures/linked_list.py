class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:
    head = None
    """
    Singly Linked List
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current:
            count+=1
            current = current.next_node

        return count

    def add(self, data):
        new_node = Node(data)

class MyClass(object):
    i = 123;
    def __init__(self):
        self.i = 345;

a = MyClass()
print(a.i)
print(MyClass.i)


