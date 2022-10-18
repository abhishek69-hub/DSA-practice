class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data)
        inorder(node.left)

        inorder(node.right)

def postorder(node):
    if node:
        inorder(node.left)

        inorder(node.right)
        print(node.data)


# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key
#
#
# # A function to do inorder tree traversal
# def printInorder(root):
#     if root:
#         # First recur on left child
#         printInorder(root.left)
#
#         # then print the data of node
#         print(root.val),
#
#         # now recur on right child
#         printInorder(root.right)
#


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(7)
root.right.right=Node(8)

inorder(root)
preorder(root)
postorder(root)