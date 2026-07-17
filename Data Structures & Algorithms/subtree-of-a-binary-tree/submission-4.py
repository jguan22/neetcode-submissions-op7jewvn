# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # this binary tree is not binary search tree
        # edge case:
        if not subRoot:
            return True
        if not root:
            return False
        
        # check curr node
        if self.isSameTree(root, subRoot):
            return True

        # if not the same, check both subtree: O(m * n)
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # helper to check if trees are the same: O(n)
    def isSameTree(self, t1, t2):
        if not t1 and not t2:
            return True
        elif not t1 or not t2:
            return False
        else:
            return t1.val == t2.val and self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)



