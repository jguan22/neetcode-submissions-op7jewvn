# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # dfs to find nums in order: O(n)
        self.k = k

        def dfs(node):
            if not node:
                return -1
            
            left = dfs(node.left)
            if self.k == 0:
                return left
            
            self.k -= 1
            if self.k == 0:
                return node.val
            
            right = dfs(node.right)
            if self.k == 0:
                return right
            
        return dfs(root)