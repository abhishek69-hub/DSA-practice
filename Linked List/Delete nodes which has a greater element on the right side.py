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

    def reverse(self):
        prev=None
        current=self.head
        next=None
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev

    def delete(self):
        temp=self.head
        max= self.head.data
        while(temp and temp.next != None ):
            if temp.next.data > max:
                max=temp.next.data
                temp=temp.next
            else:
                val=temp.next.next
                temp.next.next=None
                temp.next=val





llist=Linkedlist()

llist.push(1)
llist.push(11)
llist.push(12)
llist.push(5)
llist.push(3)
llist.push(2)
# print(llist.head.data)
llist.printlist()
llist.reverse()
llist.delete()
llist.reverse()
llist.printlist()
