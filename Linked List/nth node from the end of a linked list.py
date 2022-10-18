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

    def nthnode(self,n):
        temp=self.head
        count=1
        while(temp):
            count += 1
            temp=temp.next

        temp=self.head
        cont=1
        while(temp):
            cont=cont+1
            if cont == count-n+1:
                return temp.data
            else:
                temp=temp.next



        return temp.data

llist=Linkedlist()
llist.push(55)
llist.push(55)
llist.push(54)
llist.push(52)
llist.push(51)
llist.push(5)

llist.nthnode(2)
# llist.printlist()
print(llist.nthnode(3))




