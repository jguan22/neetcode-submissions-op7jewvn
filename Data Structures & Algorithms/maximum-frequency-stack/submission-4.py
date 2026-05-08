class FreqStack:

    def __init__(self):
        # use a stack for each freq and a dict to track freq of each num
        self.stacks = defaultdict(list)
        self.freq_map = defaultdict(int)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq_map[val] += 1
        self.stacks[self.freq_map[val]].append(val)
        
        if self.freq_map[val] > self.max_freq:
            self.max_freq = self.freq_map[val]

    def pop(self) -> int:
        val = self.stacks[self.max_freq].pop()
        self.freq_map[val] -= 1

        if len(self.stacks[self.max_freq]) == 0:
            self.max_freq -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()