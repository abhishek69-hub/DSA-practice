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

    def segregate(self):
        evenStart = None
        oddStart = None
        evenEnd = None
        oddEnd = None
        temp = self.head
        while (temp != None):
            val = temp.data
            if (val % 2 == 0):
                if (evenStart == None):
                    evenStart = temp
                    evenEnd = evenStart
                else:
                    evenEnd.next = temp
                    evenEnd = evenEnd.next
            else:
                if (oddStart == None):
                    oddStart = temp
                    oddEnd = oddStart
                else:
                    oddEnd.next = temp
                    oddEnd = oddEnd.next
            temp = temp.next
        if (oddStart == None or evenStart == None):
            return

            # Add odd list after even list.
        evenEnd.next = oddStart
        oddEnd.next = None
        self.head = evenStart

















