# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        q1=[root]
        res=[]
        q1.append(root)
        while q1:
            qlen , level = len(q1) , 0
            for i in range(qlen):
                node=q1.pop(0)
                level=float(level+node.val)
                if node.left:q1.append(node.left)
                if node.right:q1.append(node.right)
            res.append(float(level/qlen))
        return res
