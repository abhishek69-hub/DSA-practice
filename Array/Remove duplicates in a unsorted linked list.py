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
        s=set()
        ptr1=None
        while(temp and temp.next):
            if temp.next.data in s:
                ptr1=temp.next.next
                temp.next.next=None
                temp.next = ptr1
            else:
                s.add(temp.next.data)
                temp=temp.next

llist=Linkedlist()
llist.push(5)
llist.push(51)
llist.push(52)
llist.push(5)
llist.push(54)
llist.push(55)
llist.printlist()
llist.removeduplicates()
llist.printlist()
