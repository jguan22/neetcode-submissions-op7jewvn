"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        if n == 1:
            return Node(grid[0][0], True, None, None, None, None)
        
        m = n // 2
        # explore all four directions
        topLeft = self.construct([row[:m] for row in grid[:m]])
        topRight = self.construct([row[m:] for row in grid[:m]])
        bottomLeft = self.construct([row[:m] for row in grid[m:]])
        bottomRight = self.construct([row[m:] for row in grid[m:]])

        if (topLeft.isLeaf and topRight.isLeaf and 
            bottomLeft.isLeaf and bottomRight.isLeaf and
            topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
            return Node(topLeft.val, True)
        
        return Node(topLeft.val, False, topLeft, topRight, bottomLeft, bottomRight)