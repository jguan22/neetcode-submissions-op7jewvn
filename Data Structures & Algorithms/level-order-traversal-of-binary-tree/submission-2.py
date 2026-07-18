# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs: O(n)
        queue = deque([root])
        ans = []

        while queue:
            n = len(queue)
            curr_level = []

            for _ in range(n):
                node = queue.popleft()
                
                if not node:
                    continue
                curr_level.append(node.val)
                
                queue.append(node.left)
                queue.append(node.right)
            
            if curr_level:
                ans.append(curr_level)
        
        return ans