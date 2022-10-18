class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def zigzag(root):
    marker=False
    current=[]
    next=[]
    current.append(root)
    while len(current)>0:
        temp=current.pop(-1)
        print(temp.data)
        if marker is False:

            if temp.right:
                next.append(temp.right)
                if temp.left:
                    next.append(temp.left)
        else:
            if temp.left:
                next.append(temp.left)
            if temp.right:
                next.append(temp.right)

    if len(current) == 0:
        marker= not marker
        current,next=next,current


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
print("Zigzag Order traversal of binary tree is")
zigzag(root)