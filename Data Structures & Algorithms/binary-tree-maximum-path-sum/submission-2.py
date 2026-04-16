# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            # skip the negative path
            left_path = max(dfs(node.left), 0)
            right_path = max(dfs(node.right), 0)

            self.max_path_sum = max(self.max_path_sum, left_path + right_path + node.val)
            return max(left_path, right_path) + node.val
        
        dfs(root)
        return self.max_path_sum