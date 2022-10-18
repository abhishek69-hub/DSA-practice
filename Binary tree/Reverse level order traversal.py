class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def reverselevelorder(root):
    queue=[]
    queue.append(root)
    while len(queue) > 0:
        print(queue[0].data)
        pop=queue.pop(0)
        if pop.right is not None:
            queue.append(pop.right)
        if pop.left is not None:
            queue.append(pop.left)


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(7)
root.right.right=Node(8)

reverselevelorder(root)