class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def check(root):
    if root is None:
        return  True
    if root.left is None and root.right is None:
        