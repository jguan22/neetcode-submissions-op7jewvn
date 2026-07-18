# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # dfs all paths to find the max sum: O(n)
        self.max_path = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            # there could be negative path, skip it
            left_path = max(dfs(node.left), 0)
            right_path = max(dfs(node.right), 0)

            # update curr max and return max live path
            self.max_path = max(self.max_path, left_path + right_path + node.val)
            return max(left_path, right_path) + node.val
        
        dfs(root)
        return self.max_path
