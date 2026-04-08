# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        node_list = self.findNode(root, subRoot.val, [])
        for node in node_list:
            if self.isSame(node, subRoot):
                return True
        return False
    

    def findNode(self, node, val, node_list):
        if not node:
            return node_list
        
        if node.val == val:
            node_list.append(node)

        node1 = self.findNode(node.left, val, node_list)
        node2 = self.findNode(node.right, val, node_list)
        
        return node_list
    

    def isSame(self, node1, node2):
        if not node1 and not node2:
            return True
        
        if (not node1 and node2) or (not node2 and node1):
            return False
        
        if node1.val != node2.val:
            return False
        
        return self.isSame(node1.left, node2.left) and self.isSame(node1.right, node2.right)