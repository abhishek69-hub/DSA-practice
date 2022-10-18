class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def height(root):
    if root is None:
        return 0
    lheight=height(root.left)
    rheight=height(root.right)
    if lheight > rheight:
        return lheight
    else:
        return rheight

def checkbalance(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)

    if (abs(lh - rh) <= 1):
        if checkbalance(root.left) is True:
            if checkbalance(root.right) is True:
                return True
    return False
