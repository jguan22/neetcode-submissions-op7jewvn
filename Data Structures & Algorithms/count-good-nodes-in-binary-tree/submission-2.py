# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs to the node and provide the path max: O(n)
        def dfs(node, path_max):
            if not node:
                return 0
            
            count = 0
            if node.val >= path_max:
                count += 1
                path_max = node.val
            
            count += dfs(node.left, path_max)
            count += dfs(node.right, path_max)
            return count

        return dfs(root, root.val)