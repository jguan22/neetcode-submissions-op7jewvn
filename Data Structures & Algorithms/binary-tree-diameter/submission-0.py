# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth, diameter = self.DFS(root)
        return diameter

    
    def DFS(self, node):
        if node is None:
            return 0, 0
        
        left_len, left_dia = self.DFS(node.left)
        right_len, right_dia = self.DFS(node.right)
        max_len = max(left_len, right_len) + 1

        curr_dia = left_len + right_len
        max_dia = max(left_dia, right_dia, curr_dia)

        return max_len, max_dia