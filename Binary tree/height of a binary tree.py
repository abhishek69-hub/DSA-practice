class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def height(root):
    if root is None:
        return 0
    else:
        ldepth=height(root.left)
        rdepth=height(root.right)

        if ldepth > rdepth:
            return ldepth+1
        else:
            return rdepth+1

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(7)
root.right.right=Node(8)

print(height(root))