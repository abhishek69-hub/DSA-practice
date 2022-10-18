class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def height(node):
    if node is None:
        return 0
    ldepth=height(node.left)
    rdepth=height(node.right)

    if ldepth>rdepth:
        return ldepth + 1
    else:
        return rdepth + 1


def diameter(node):
    a=height(node.left)
    b=height(node.right)
    c=a+b+1
    return c










root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(7)
root.right.right=Node(8)

print(diameter(root))