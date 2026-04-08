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
            
        # use BFS(inorder), easier to show the shape and when to stop
        # separate nodes by ','
        # use 'n' for empty node
        queue = deque([root])
        node_list = []

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node is None:
                    node_list.append("n")
                else:
                    node_list.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                
        return ",".join(node_list)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        node_list = data.split(",")
        root = TreeNode(int(node_list[0]))
        queue = deque([root])

        i = 1
        while queue:
            node = queue.popleft()
            if node_list[i] != "n":
                left_node = TreeNode(int(node_list[i]))
                node.left = left_node
                queue.append(left_node)
            i += 1
            
            if node_list[i] != "n":
                right_node = TreeNode(int(node_list[i]))
                node.right = right_node
                queue.append(right_node)
            i += 1
        
        return root
