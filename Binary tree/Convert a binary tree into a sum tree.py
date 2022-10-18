class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def tosumtree(root):
    if root is None:
        return 0
    old_data=root.data
    root.data=tosumtree(root.left)+tosumtree(root.right)
    return root.data+old_data

def inorder(root):
    if root is None:
        return None
    inorder(root.left)
    print(root.data)
    inorder(root.right)



root=Node(10)
root.left=Node(-2)
root.right=Node(6)
root.left.left=Node(8)
root.left.right=Node(-4)
root.right.left=Node(7)
root.right.right=Node(5)

tosumtree(root)
inorder(root)