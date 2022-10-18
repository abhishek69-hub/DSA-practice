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

    def removeduplicates(self):
        temp=self.head
        s = set()
        while(temp.next != None):

            if temp.next.data in s:
                temp.next=temp.next.next
            else:
                s.add(temp.next.data)
                temp=temp.next

llist=Linkedlist()
llist.push(5)
llist.push(51)
llist.push(52)
llist.push(53)
llist.push(51)
llist.push(55)
llist.push(56)

llist.printlist()
llist.removeduplicates()
llist.printlist()

