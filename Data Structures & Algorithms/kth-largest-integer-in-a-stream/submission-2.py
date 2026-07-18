class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # use a min heap and keep size at k: O(nlogk)
        self.min_heap = nums
        self.size = k
        heapq.heapify(self.min_heap)
        self.pop()

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        self.pop()
        return self.min_heap[0]

    def pop(self):
        while len(self.min_heap) > self.size:
            heapq.heappop(self.min_heap)