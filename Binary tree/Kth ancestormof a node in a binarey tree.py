class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def kthancestor(root,k,node):
    if root is None:
        return None

    if root.data == node:
        if k == 0:
            return root.data
        k=k-1
        return None
    kthancestor(root.left, k, node)
    kthancestor(root.right, k, node)


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
print(kthancestor(root,2,7))
