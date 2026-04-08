# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k

        def dfs(node):
            if not node:
                return
            
            left = dfs(node.left)
            if self.k == 0:
                return left
            
            self.k -= 1
            if self.k == 0:
                return node.val
            
            right = dfs(node.right)
            if self.k == 0:
                return right
            
            return
        
        return dfs(root)