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
            print(temp)
            temp=temp.next

    def detectloop(self):
        s=set()
        temp=self.head
        while(temp):
            if temp in s:
                return True
            s.add(temp)
            temp=temp.next
        return False


llist=Linkedlist()
llist.push(5)
llist.push(51)
llist.push(52)
llist.push(53)
llist.push(54)
llist.push(55)
llist.push(56)
llist.push(57)
llist.push(58)
llist.push(59)



llist.head.next.next.next = llist.head.next


if(llist.detectloop()):
    print("loop detected")
else:
    print("loop not found")

