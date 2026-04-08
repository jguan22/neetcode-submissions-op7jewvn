class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # use min heap
        self.heap = nums
        self.k = k
        
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
            

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # keep heap with size k    
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
        
