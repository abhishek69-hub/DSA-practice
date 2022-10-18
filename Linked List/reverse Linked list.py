class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def insert(self,data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    def printdata(self):
        if self.head is None:
            print("Linked list is empty")
        elem=self.head
        while self.head:
            print(elem.data)
            elem=elem.next
    def reverseLL(self):
        previous=None
        current=self.head
        next=None
        count=0
        while (current is not None):
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous



LL=Linkedlist()
LL.insert(5)
LL.insert(51)
LL.insert(52)
LL.reverseLL()

LL.printdata()