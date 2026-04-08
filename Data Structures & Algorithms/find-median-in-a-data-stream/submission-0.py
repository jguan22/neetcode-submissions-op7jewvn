class MedianFinder:

    def __init__(self):
        # maintain one max heap and one min heap
        # max_heap for the smaller half
        # min_heap for the larger half
        # median will be the top of two heaps
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        # ensure top of max_heap is smaller than min_heap
        if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            n = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, n)
        
        # keep the size of heap the same
        if len(self.max_heap) > len(self.min_heap) + 1:
            n = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, n)
        elif len(self.min_heap) > len(self.max_heap):
            n = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -n)
        

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            num1 = self.min_heap[0]
            num2 = -self.max_heap[0]
            return (num1 + num2) / 2
        else:
            num = -self.max_heap[0]
            return num
        
        