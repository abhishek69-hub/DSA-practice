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

    def addone(self):
        self.reverse()

        if self.head.data != 9:
            self.head.data += 1
            return Linkedlist
        else:
            temp = self.head
            carry = 1
            while (temp.data):
                if(temp.next != None):
                    temp.data += carry
                    carry = temp.data // 10
                    temp.data = temp.data % 10
                    temp = temp.next
                else:
                    temp.data += carry
                    carry = temp.data // 10
                    temp.data = temp.data % 10
                    newnode=Node(carry)
                    temp.next=newnode
        return








llist=Linkedlist()
llist.push(9)
llist.push(0)
llist.push(3)
llist.printlist()
llist.addone()
llist.reverse()
llist.printlist()

