# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs: O(n)
        queue = deque([root])
        ans = []

        while queue:
            right_node = None
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()
                if node:
                    right_node = node
                    queue.append(node.left)
                    queue.append(node.right)
            
            if right_node:
                ans.append(right_node.val)
        
        return ans