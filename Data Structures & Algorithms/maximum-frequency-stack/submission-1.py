class FreqStack:

    def __init__(self):
        # use a stack of stacks to track freq and sequence
        self.freq_dict = defaultdict(int)
        self.stack = defaultdict(list)
        self.max_freq = 0
        
    def push(self, val: int) -> None:
        # update freq of val
        self.freq_dict[val] += 1
        freq = self.freq_dict[val]
        if freq > self.max_freq:
            self.max_freq = freq

        # push it to the corresponding stack
        self.stack[freq].append(val)

    def pop(self) -> int:
        # pop val from the top of the stack on the list
        val = self.stack[self.max_freq].pop()

        # update the freq and stack if necessary
        self.freq_dict[val] -= 1
        if not self.stack[self.max_freq]:
            self.max_freq -= 1
        
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()