# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # find the node first, then delete it and promote one of its children
        # choices are the largest one on left or smallest one on right
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # find the node with less than two children
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # find the In-order Successor (smallest in the right subtree)
            successor = self.getMin(root.right)
            root.val = successor.val
            
            # delete the successor node from the right subtree
            root.right = self.deleteNode(root.right, successor.val)
            
        return root

    def getMin(self, node):
        while node.left:
            node = node.left
        return node