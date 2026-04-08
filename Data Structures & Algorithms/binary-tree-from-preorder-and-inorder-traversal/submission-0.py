# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
            
        # first val in preorder must be the root
        # anything before root in inorder is left subtree nodes
        # the rest is right subtree nodes
        root_val = preorder[0]
        root = TreeNode(root_val)

        # if only right tree
        if inorder[0] == root_val:
            right_tree = self.buildTree(preorder[1:], inorder[1:])
            root.right = right_tree
            return root

        # if only left tree
        if inorder[-1] == root_val:
            left_tree = self.buildTree(preorder[1:], inorder[:-1])
            root.left = left_tree
            return root

        i = 0
        while inorder[i] != root_val:
            i += 1
        
        
        preorder_left = preorder[1:i+1]
        preorder_right = preorder[i+1:]
        inorder_left = inorder[:i]
        inorder_right = inorder[i+1:]

        left_tree = self.buildTree(preorder_left, inorder_left)
        right_tree = self.buildTree(preorder_right, inorder_right)
        root.left = left_tree
        root.right = right_tree

        return root