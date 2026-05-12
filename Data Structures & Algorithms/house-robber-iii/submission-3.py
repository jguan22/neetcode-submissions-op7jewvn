# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]   # (skip, include)
            
            # either rob curr one or skip it
            left = dfs(node.left)
            right = dfs(node.right)

            skip = max(left) + max(right)
            include = left[0] + right[0] + node.val
            return [skip, include]
        
        return max(dfs(root))