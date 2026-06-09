class MedianFinder:

    def __init__(self):
        # use a max_heap for lower half and a min_heap for higher half
        # so, it takes constant time to find median
        self.min_heap = []
        self.max_heap = []
        
    def addNum(self, num: int) -> None:
        if not self.min_heap or num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -1*num)
        
        self.__balance()

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        
    def __balance(self):
        if len(self.min_heap) > len(self.max_heap) + 1:
            num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1*num)
        elif len(self.max_heap) > len(self.min_heap):
            num = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -1*num)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()