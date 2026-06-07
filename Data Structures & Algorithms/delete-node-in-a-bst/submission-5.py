# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return None
        
        # find target node
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # find the node, now rebuild the subtree
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # if node has both left and right, move largest from left here
                next_val = self.findLargestOnLeft(root)
                root.val = next_val
                root.left = self.deleteNode(root.left, next_val)
        return root

    def findLargestOnLeft(self, node):
        curr = node.left
        while curr.right:
            curr = curr.right
        return curr.val