# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # build a map from val to index for fast retrieval
        index_map = {val: i for i, val in enumerate(inorder)}

        def build(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            inorder_root_index = index_map[root_val]
            left_size = inorder_root_index - in_left
            root.left = build(pre_left + 1, pre_left + left_size, in_left, inorder_root_index)
            root.right = build(pre_left + left_size + 1, pre_right, inorder_root_index + 1, in_right)

            return root
        
        return build(0, len(preorder) - 1, 0, len(preorder) - 1)