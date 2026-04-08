# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            
            left = compare(n1.left, n2.left)
            right = compare(n1.right, n2.right)
            return left and right and n1.val == n2.val
        
        def dfs(node, target):
            if not node:
                return False
            
            if compare(node, target):
                return True
            
            return dfs(node.left, target) or dfs(node.right, target)
        
        return dfs(root, subRoot)