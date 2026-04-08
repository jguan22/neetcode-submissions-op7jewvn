# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # curr max = max(curr one + max of n-2, max of n-1)
        # thus, for each node, we need to return two values
        def dfs(node):
            if not node:
                # [max with curr, max without curr]
                return [0, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)
            max_with_curr = node.val + left[1] + right[1]
            max_without_curr = max(left) + max(right)
            return [max_with_curr, max_without_curr]
        
        root_max = dfs(root)
        return max(root_max)