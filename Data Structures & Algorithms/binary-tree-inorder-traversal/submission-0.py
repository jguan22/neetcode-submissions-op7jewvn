# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return []
            
            res = []
            left = dfs(node.left)
            res.extend(left)
            res.append(node.val)
            right = dfs(node.right)
            res.extend(right)

            return res

        return dfs(root)