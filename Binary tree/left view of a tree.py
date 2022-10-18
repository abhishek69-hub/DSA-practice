class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def leftview(root):
    if root is None:
        return
    else:
        print(root.data)
        leftview(root.right)


node=Node(1)
node.left=Node(2)
node.right=Node(3)
node.left.left=Node(4)
node.left.right=Node(5)
node.right.left=Node(6)
node.right.right=Node(7)

leftview(node)
