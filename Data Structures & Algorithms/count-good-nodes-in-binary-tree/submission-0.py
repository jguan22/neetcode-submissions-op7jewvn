# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # keep tracking the max value as DFS goes
        res = self.DFS(root, root.val)
        return res


    def DFS(self, node, max_val):
        if node is None:
            return 0

        good = 0
        if node.val >= max_val:
            max_val = node.val
            good += 1
        
        good += self.DFS(node.left, max_val)
        good += self.DFS(node.right, max_val)
        return good