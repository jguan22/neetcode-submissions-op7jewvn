# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # its a binary search tree
        curr = root
        if p.val > q.val:
            p, q = q, p

        while True:
            # one of nodes is the ancestor of another
            if curr.val == p.val or curr.val == q.val:
                return curr
            
            # the path split here, curr is the lca
            if p.val < curr.val < q.val:
                return curr
            
            if curr.val > q.val:
                curr = curr.left
            else:
                curr = curr.right