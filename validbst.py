# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        return self.dfs(root,float("-inf"),float("inf"))

    def dfs(self,root,min,max):
        if not root:
            return True
        if root.val<=min or root.val>=max:
            return False
        else:
            return self.dfs(root.left,min,root.val) and self.dfs(root.right,root.val,max)
        
