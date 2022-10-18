class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def checkbst(root):
    if root is None:
        return True
    if root.data < root.left.data:
        return False
    if root.data > root.right.data:
        return False
    if !(checkbst(root.left) and checkbst(root.right)):
        return False


root=Node(12)
root.left=Node(9)
root.right=Node(20)
root.left.left=Node(6)
root.left.right=Node(10)
root.right.left=Node(16)
root.right.right=Node(27)

print(checkbst(root))