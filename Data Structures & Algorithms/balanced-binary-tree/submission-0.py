# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # check depth of two subtrees
        depth, isBalanced = self.DFS(root)
        return isBalanced

        
    def DFS(self, node):
        if node is None:
            return 0, True
        
        left, leftBalanced = self.DFS(node.left)
        right, rightBalanced = self.DFS(node.right)

        depth = max(left, right)
        isBalanced = True if leftBalanced and rightBalanced else False

        if depth - left > 1 or depth - right > 1:
            isBalanced = False

        return depth + 1, isBalanced