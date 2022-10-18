class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def lca(root,a,b):
    if root == None:
        return None
    if root.data == a or root.data==b:
        return root

    leftlca=lca(root.left,a,b)
    rightlca=lca(root.right,a,b)

    if leftlca and rightlca:
        return root.data
    if leftlca:
        return leftlca.data
    if rightlca:
        return rightlca.data


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

print(lca(root,2,4))
