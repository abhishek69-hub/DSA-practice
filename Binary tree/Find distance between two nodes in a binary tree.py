class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def lca(root,n1,n2):
    if root is None:
        return None
    if root.data == n1:
        return root
    if root.data==n2:
        return root

    leftlca=lca(root.left,n1,n2)
    rightlca=lca(root.right,n1,n2)

    if leftlca and rightlca:
        return root
    if leftlca:
        return leftlca
    if rightlca:
        return rightlca

def distancefromroot(root,n):
    if root is None:
        return -1
    if root.data == n:
        return 0
    ld=distancefromroot(root.left,n)
    rd=distancefromroot(root.right,n)
    distance=max(ld,rd)
    return distance + 1 if distance > 0 else -1

def distancebetweennodes(n1,n2):
    lca1=lca(root,n1,n2)
    return distancefromroot(lca1,n1)+distancefromroot(lca1,n2)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

print(distancebetweennodes(2,6))
