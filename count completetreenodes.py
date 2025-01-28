# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        count=0
        if root:
            count+=1
        count+=self.countNodes(root.left)
        count+=self.countNodes(root.right)
        return count
