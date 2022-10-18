class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def mirrorimages(root,root2):
    if root is None and root2 is not None:
        return False
    if root2 is None and root is not None:
        return False
    if root.data == root2.data and mirrorimages(root.left,root2.right) and mirrorimages(root.right,root2.left):
        return True
