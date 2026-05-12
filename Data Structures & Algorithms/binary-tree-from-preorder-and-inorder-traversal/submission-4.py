# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # use an index map to map num to inorder index
        index_map = {num: i for i, num in enumerate(inorder)}

        def build(pre_left, pre_right, in_left, in_right):
            # base case: done when left > right:
            if pre_left > pre_right:
                return None
            
            # first num in preorder is root
            root = TreeNode(preorder[pre_left])
            root_index = index_map[root.val]
            left_len = root_index - in_left
            
            # build left and right subtrees
            root.left = build(pre_left + 1, pre_left + left_len, in_left, root_index - 1)
            root.right = build(pre_left + left_len + 1, pre_right, root_index + 1, in_right)
        
            return root
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)