# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append('N')
                continue
            
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        tree_str = data.split(',')
        root = TreeNode(int(tree_str[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()

            if tree_str[i] != 'N':
                left = TreeNode(int(tree_str[i]))
                node.left = left
                queue.append(left)
            
            if tree_str[i+1] != 'N':
                right = TreeNode(int(tree_str[i+1]))
                node.right = right
                queue.append(right)
            
            i += 2
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))