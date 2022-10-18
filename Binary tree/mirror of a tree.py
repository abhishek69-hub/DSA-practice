class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def mirror(root):
    if root is None:
        return
    mirror(root.left)
    mirror(root.right)

    temp=root.left
    root.left=root.right
    root.right=temp

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

inorder(root)
print("yes now see the chnage bitch")
mirror(root)
inorder(root)
