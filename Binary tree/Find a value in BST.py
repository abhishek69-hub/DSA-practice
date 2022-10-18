class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def search(root,data):
    if root is None:
        return None
    if root.data == data:
        return root
    if root.data > data:
        search(root.left,data)
    search(root.right,data)