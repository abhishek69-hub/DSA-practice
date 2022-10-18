class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def sumandheight(root):
    if root is None:
        return 0,0
    else:
        lheight=sumandheight(root.left)
        rheight = sumandheight(root.right)

        if lheight > rheight:
            return lheight+1,



