class FreqStack:

    def __init__(self):
        # use freq dict and max heap (-freq, -index, num)
        self.freq_dict = defaultdict(int)
        self.max_heap = []
        self.index = 0
        
    def push(self, val: int) -> None:
        # If there is a tie, return num that closer to the stack's top
        self.freq_dict[val] += 1
        heapq.heappush(self.max_heap, (self.freq_dict[val] * -1, self.index * -1, val))
        self.index += 1

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.max_heap)
        self.freq_dict[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()