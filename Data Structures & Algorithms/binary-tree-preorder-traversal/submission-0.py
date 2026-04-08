# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return []
            
            res = []
            res.append(node.val)
            res.extend(dfs(node.left))
            res.extend(dfs(node.right))

            return res
        
        return dfs(root)