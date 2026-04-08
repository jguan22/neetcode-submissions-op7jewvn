# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_p = self.DFS(root, p.val, [])
        path_q = self.DFS(root, q.val, [])
        LCA = root

        while path_p and path_q and path_p[-1] == path_q[-1]:
            LCA = path_p[-1]
            path_p.pop()
            path_q.pop()
        
        return LCA
        

    def DFS(self, node, val, path):
        if node is None:
            return path
        
        if node.val == val:
            path.append(node)
            return path
        
        path1 = self.DFS(node.left, val, path)
        if path1 and path1[0].val == val:
            path1.append(node)
            return path1

        path2 = self.DFS(node.right, val, path)
        if path2 and path2[0].val == val:
            path2.append(node)
            return path2