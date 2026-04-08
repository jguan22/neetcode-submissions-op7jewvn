class FreqStack:

    def __init__(self):
        self.stacks = defaultdict(list)
        self.freq_map = defaultdict(int)
        self.max_freq = 0
        

    def push(self, val: int) -> None:
        self.freq_map[val] += 1
        if self.freq_map[val] > self.max_freq:
            self.max_freq = self.freq_map[val]
        
        self.stacks[self.freq_map[val]].append(val)

    def pop(self) -> int:
        val = self.stacks[self.max_freq].pop()
        self.freq_map[val] -= 1
        
        if not self.stacks[self.max_freq]:
            self.max_freq -= 1
        
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()