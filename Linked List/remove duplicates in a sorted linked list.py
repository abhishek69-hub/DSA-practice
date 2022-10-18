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
        while(temp.next != None):
            if temp.data == temp.next.data:
                temp.next=temp.next.next
            else:
                temp=temp.next



llist=Linkedlist()
llist.push(56)
llist.push(55)
llist.push(54)
llist.push(52)
llist.push(52)
llist.push(5)




llist.removeduplicates()

llist.printlist()