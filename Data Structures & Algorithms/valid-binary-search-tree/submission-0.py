# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # use DFS
        isValid, minVal, maxVal = self.DFS(root)
        return isValid
    

    def DFS(self, node):
        min_val = max_val = node.val
        isValidLeft = isValidRight = True
        if node.left:
            isValidLeft, min_left, max_left = self.DFS(node.left)
            if node.val <= max_left:
                return False, -1, -1
            min_val = min(min_val, min_left)
        
        if node.right:
            isValidRight, min_right, max_right = self.DFS(node.right)
            if node.val >= min_right:
                return False, -1, -1
            max_val = max(max_val, max_right)
        
        return isValidLeft and isValidRight, min_val, max_val