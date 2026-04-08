# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # find the root of curr tree
        # split to left and right subtrees
        # build them recursively

        # base case:
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])

        # find the index of root in inorder
        i = 0
        while inorder[i] != preorder[0]:
            i += 1
        
        # preorder: left [1:i]
        # inorder: left [:i], right [i+1:]
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])

        return root