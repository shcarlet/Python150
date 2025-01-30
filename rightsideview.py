# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        queue = deque([root])
        queue.append(root)
        res = []
        while queue:
            right = None
            length = len(queue)
            for i in range (length):
                node = queue.popleft()
                if node:
                    right = node
                    queue.append(node.left)
                    queue.append(node.right)
            if right:
                res.append(right.val)
        return res 

        
