class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def sum(root):
    if root is None:
        return 0
    lsum=sum(root.left)
    rsum=sum(root.right)
    return  lsum+rsum+root.data

def check(root):
    if (root == None or
            (root.left == None and
             root.right == None)):
        return True
    ls=sum(root.left)
    rs=sum(root.right)
    if root.data == ls+rs and check(root.left) and check(root.right):
        return True
    return False


root = node(26)
root.left = node(10)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(6)
root.right.right = node(3)
print(check(root))