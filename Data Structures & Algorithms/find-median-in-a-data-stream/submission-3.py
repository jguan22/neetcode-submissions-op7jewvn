class MedianFinder:

    def __init__(self):
        # use two heaps: min_heap for larger half and max_heap for smaller half
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap or num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        self.__balance()

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            median = (self.min_heap[0] - self.max_heap[0]) / 2.0
            return median

    def __balance(self):
        if len(self.min_heap) > len(self.max_heap) + 1:
            num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -num)
        elif len(self.min_heap) < len(self.max_heap):
            num = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -num)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()