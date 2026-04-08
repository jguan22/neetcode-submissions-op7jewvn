class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        max_heap = []
        
        for num in nums:
            freq[num] += 1
        
        for num in freq:
            heapq.heappush(max_heap, (-freq[num], num))
        
        ans = []
        for i in range(k):
            number = heapq.heappop(max_heap)[1]
            ans.append(number)

        return ans