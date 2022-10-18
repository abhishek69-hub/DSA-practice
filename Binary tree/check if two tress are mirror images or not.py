class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def check(a,b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if (a.data == b.data and check(a.right,b.left) and check(a.left,b.right)):
        return True
a= None
b=Node(5)
print(check(a,b))