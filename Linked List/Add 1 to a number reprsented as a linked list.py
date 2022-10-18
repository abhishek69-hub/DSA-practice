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

    def addOne(self):
        self.reverse()
        temp=self.head
        prev=None
        carry=0
        temp.data += 1
        while(temp != None) and (temp.data > 9 or carry > 0):
            prev=temp
            temp.data += carry
            carry = temp.data // 10
            temp.data =temp.data % 10
            temp=temp.next

        if carry > 0:
            prev.next=Node(carry)
        return self.reverse()


llist=Linkedlist()
llist.push(9)
llist.push(9)
llist.push(9)
llist.printlist()
llist.addOne()
llist.printlist()



