class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        heap = []
        for num in freq_map:
            heapq.heappush(heap, [-freq_map[num], num])
        
        res = []
        for i in range(k):
            value = heapq.heappop(heap)
            res.append(value[1])
        
        return res