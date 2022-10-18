# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.right=None
#         self.left=None
# ans=[-9999999999999]
# def maxsumutil(root,ans):
#     if root is None:
#         return 0
#     lsum=maxsumutil(root.left,ans)
#     rsum=maxsumutil(root.right,ans)
#
#     currsum=root.data+lsum+rsum
#     ans[0]=max(currsum,ans[0])
#
#     return currsum
#
# # def maxsum(root):
# #     if root is None:
# #         return 0
# #     ans=[-9999999999999]
# #     return maxsumutil(root,ans)
#
#
# root=Node(1)
# root.left=Node(2)
# root.right=Node(3)
# root.left.left=Node(4)
# root.left.right=Node(5)
# root.right.left=Node(6)
# root.right.right=Node(7)
#
# print(maxsumutil(root,ans))


class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
ans=[-9999999999999]
def maxsumutil(root,ans):
    if root is None:
        return 0
    lsum=maxsumutil(root.left,ans)
    rsum=maxsumutil(root.right,ans)

    currsum=root.data+lsum+rsum
    ans[0]=max(currsum,ans[0])

    return currsum

def maxsum(root):
    if root is None:
        return 0
    ans=[-9999999999999]
    return maxsumutil(root,ans)


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

print(maxsum(root))