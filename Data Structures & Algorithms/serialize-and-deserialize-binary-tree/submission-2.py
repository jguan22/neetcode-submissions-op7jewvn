# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        tree = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                tree.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                tree.append('N')

        return ",".join(tree)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        
        def makeNode(value):
            if value == 'N':
                return None
            return TreeNode(int(value))

        node_list = data.split(',')
        root = TreeNode(int(node_list[0]))
        queue = deque([root])
        i = 1
        while i < len(node_list):
            curr = queue.popleft()
            left = makeNode(node_list[i])
            if left:
                curr.left = left
                queue.append(left)
            i += 1

            right = makeNode(node_list[i])
            if right:
                curr.right = right
                queue.append(right)
            i += 1
        
        return root
