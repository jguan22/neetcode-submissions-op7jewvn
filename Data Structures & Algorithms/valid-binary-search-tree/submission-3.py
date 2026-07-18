# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # dfs and provide upper and lower bound of valid range: O(n)
        def isValid(node, low, high):
            if not node:
                return True
            
            if node.val >= high or node.val <= low:
                return False
            
            return isValid(node.left, low, node.val) and isValid(node.right, node.val, high)
        
        return isValid(root, float('-inf'), float('inf'))