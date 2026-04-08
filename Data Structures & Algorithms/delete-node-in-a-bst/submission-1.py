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

        # node is on the left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # node is on the right
            root.right = self.deleteNode(root.right, key)
        else:
            # find the node with less than two children
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # node with two children
            # look for the largest on the left
            node = self.getMax(root.left)
            root.val = node.val

            # delete the selected node
            root.left = self.deleteNode(root.left, node.val)
        
        return root


    def getMax(self, node):
        while node.right:
            node = node.right
        return node
