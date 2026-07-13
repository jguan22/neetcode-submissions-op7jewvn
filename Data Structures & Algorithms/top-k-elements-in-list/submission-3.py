class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the list: O(n)
        freq_map = Counter(nums)
        max_heap = [(-freq, num) for num, freq in freq_map.items()]
        
        # use a heap: O(nlogn)
        heapq.heapify(max_heap)
        ans = []
        for _ in range(k):
            _, num = heapq.heappop(max_heap)
            ans.append(num)

        return ans