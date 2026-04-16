# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # helper method to return max with curr node and max without curr node
        def dfs(node):
            if not node:
                return [0, 0]
            
            left_max = dfs(node.left)
            right_max = dfs(node.right)

            max_with = node.val + left_max[1] + right_max[1]
            max_without = max(left_max) + max(right_max)
            return [max_with, max_without]
            
        root_max = dfs(root)
        return max(root_max)