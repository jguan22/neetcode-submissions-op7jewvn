# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # dp problem: need to dfs and return max path sum and curr path
        # keep track of the global max
        self.maxPathSum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # can choose to not include any neg path
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            currPath = max(left, right) + node.val

            self.maxPathSum = max(self.maxPathSum, left + right + node.val)
            return currPath

        dfs(root)
        return self.maxPathSum