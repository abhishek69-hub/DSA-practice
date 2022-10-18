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


    def ispalindrome(self):
        stack=[]
        temp=self.head
        while(temp):
            stack.append(temp.data)
            temp=temp.next
        temp1=self.head
        while(temp1):
            i=stack.pop()
            if i == temp1.data:
                return True
            else:
                return False



ll=Linkedlist()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(2)
ll.push(1)


if ll.ispalindrome() == True:
    print("True")

