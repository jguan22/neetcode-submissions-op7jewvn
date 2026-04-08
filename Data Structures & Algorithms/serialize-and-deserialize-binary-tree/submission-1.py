# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        # use inorder
        queue = deque([root])
        res = []
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node is None:
                    res.append('n')
                else:
                    res.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
        
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        # helper
        def makeNode(string):
            if string == 'n':
                return None
            return TreeNode(int(string))


        # parse the string to list
        nodeList = data.split(',')
        root = TreeNode(int(nodeList[0]))
        queue = deque([root])
        
        i = 1
        while queue:
            node = queue.popleft()
            left = makeNode(nodeList[i])
            node.left = left
            if left is not None:
                queue.append(left)
            i += 1

            right = makeNode(nodeList[i])
            node.right = right
            if right is not None:
                queue.append(right)
            i += 1
        
        return root
