class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def lefttraversal(root):
    if root is None:
        return
    else:
        print(root.data)
        lefttraversal(root.left)

def righttraversal(root1):
    if root is None:
        return
    else:
        lefttraversal(root1.right)
        print(root1.data)

def rootnodes(root):
    if root.left is None and root.right is None:
        print(root.data)
    else:
        rootnodes(root.left)
        rootnodes(root.right)



root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

lefttraversal(root)
rootnodes(root)
righttraversal(root)