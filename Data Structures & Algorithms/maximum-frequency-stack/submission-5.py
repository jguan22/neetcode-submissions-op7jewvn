class FreqStack:

    def __init__(self):
        # need stacks to store num with the same freq
        # need a dict to track freq and a dict to map freq to stack
        self.freq_map = defaultdict(int)
        self.stack_map = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        # update freq of val and insert into stack
        self.freq_map[val] += 1
        self.stack_map[self.freq_map[val]].append(val)

        # update max freq if necessary
        if self.freq_map[val] > self.max_freq:
            self.max_freq += 1

    def pop(self) -> int:
        # pop val from most freq stack
        val = self.stack_map[self.max_freq].pop()
        self.freq_map[val] -= 1

        # update max freq if necessary
        if len(self.stack_map[self.max_freq]) == 0:
            self.max_freq -= 1

        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()