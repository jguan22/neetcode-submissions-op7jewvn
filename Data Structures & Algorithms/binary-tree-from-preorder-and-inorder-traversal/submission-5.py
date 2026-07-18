# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # build the tree by locating the root and constructing the left and right tree recursively: O(n)
        # precompute the dict to map num to inorder index
        inorder_map = {num: i for i, num in enumerate(inorder)}

        def constructTree(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            
            # root is the first on in preorder
            root = TreeNode(preorder[pre_left])
            root_i = inorder_map[root.val]
            left_len = root_i - in_left

            # build left and right subtrees
            root.left = constructTree(pre_left+1, pre_left+left_len, in_left, root_i-1)
            root.right = constructTree(pre_left+left_len+1, pre_right, root_i+1, in_right)
            return root
        
        return constructTree(0, len(preorder) - 1, 0, len(inorder) - 1)