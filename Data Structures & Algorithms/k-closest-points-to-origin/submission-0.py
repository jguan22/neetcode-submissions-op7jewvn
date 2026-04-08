class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(min_heap, (dist, point))
        
        # kth closest point = kth smallest distance
        # need to track the dist as pop goes to keep points with same dist
        res = []
        max_dist = 0
        for _ in range(k):
            dist, point = heapq.heappop(min_heap)
            res.append(point)

        # keep going until we have all points    
        while min_heap and min_heap[0][0] == dist:
            _, p = heapq.heappop(min_heap)
            res.append(p)

        return res