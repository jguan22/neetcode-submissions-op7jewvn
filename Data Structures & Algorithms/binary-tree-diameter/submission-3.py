# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        # dfs the tree and update the path length: O(n)
        def dfs(node):
            if not node:
                return 0
            
            left_len = dfs(node.left)
            right_len = dfs(node.right)

            # update the diameter
            self.diameter = max(self.diameter, left_len + right_len)

            # return longest path to curr node
            return max(left_len, right_len) + 1
        
        dfs(root)
        return self.diameter