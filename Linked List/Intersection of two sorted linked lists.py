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

def intersection(a,b):
    c = Linkedlist()
    temp1 = a.head
    temp2 = b.head
    while (temp1 and temp2):
        if (temp1.data == temp2.data):
            newnode = Node(temp1.data)
            c.push(newnode)
            temp1 = temp1.next;
            temp2 = temp2.next;

        # advance the smaller list
        elif (temp1.data < temp2.data):
            temp1 = temp1.next;
        else:
            temp2 = temp2.next

    c.printlist()





a=Linkedlist()
b=Linkedlist()

a.push(1)
a.push(2)
a.push(11)
a.push(12)
a.push(13)
a.push(14)

b.push(3)
b.push(4)
b.push(11)
b.push(12)
b.push(13)
b.push(14)

intersection(a,b)














