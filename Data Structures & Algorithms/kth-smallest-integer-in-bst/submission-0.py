# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        res = -1
        
        def DFS(node):
            nonlocal n, res
            if node is None or n >= k:
                return
            
            DFS(node.left)
            n += 1
            if n == k:
                res = node.val
                return
            DFS(node.right)
        
        DFS(root)
        return res