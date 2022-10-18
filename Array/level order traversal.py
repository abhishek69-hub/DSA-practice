class Node:
    def __init__(self,data1):
        self.data=data1
        self.left=None
        self.right=None

def levelorder(root):
    # print(root.data,end=" ")
    queue=[]
    queue.append(root)
    while len(queue)>0:
        print(queue[0].data)
        node=queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)



root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

levelorder(root)
# print(root.left.right.data)












































# def printTree(root):
#     if root == None:
#         return None
#     print(root.data)
#     if root.left:
#         printTree(root.left)
#     if root.right:
#         printTree(root.right)

