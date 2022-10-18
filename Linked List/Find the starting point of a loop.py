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

    def findStart(self):
        s=set()
        temp=self.head
        while(temp):
            if temp in s:
                print(temp.data)
                break
            else:
                s.add(temp)
                temp=temp.next
                continue



llist=Linkedlist()
llist.push(5)
llist.push(51)
llist.push(52)
llist.push(53)
llist.push(54)
llist.push(55)



llist.printlist()
llist.head.next.next.next.next.next.next = llist.head.next.next
llist.findStart()

