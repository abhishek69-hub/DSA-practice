class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def push(self,data):
        newnode=Node(data)
        if(self.head):
            newnode.next=self.head
            self.head=newnode
        else:
            self.head=newnode

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def move(self):
        temp=self.head
        while(temp.next):
            if(temp.next.next == None):
                node1 = temp.next
                temp.next = None
                node1.next=self.head
                self.head= node1
            else:
                temp = temp.next

llist=Linkedlist()
llist.push(55)
llist.push(55)
llist.push(54)
llist.push(52)
llist.push(51)
llist.push(5)
# llist.printlist()
llist.move()
llist.printlist()

