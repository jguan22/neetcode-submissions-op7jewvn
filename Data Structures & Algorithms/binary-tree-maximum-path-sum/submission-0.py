# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # use DFS to return both curr path and max path sum of curr subtree
        _, max_sum = self.DFS(root)
        return max_sum

    
    def DFS(self, node):
        if node is None:
            return 0, float('-inf')
        
        left_path, left_sum = self.DFS(node.left)
        right_path, right_sum = self.DFS(node.right)

        # Can choose to not include negative branches
        left_path = max(left_path, 0)
        right_path = max(right_path, 0)

        best_path = max(left_path, right_path) + node.val
        max_sum = max(left_sum, right_sum)
        max_sum = max(max_sum, left_path + right_path + node.val)

        return best_path, max_sum