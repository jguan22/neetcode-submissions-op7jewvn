class FreqStack:

    def __init__(self):
        # use stack of stacks
        # pop from top stack first
        self.stacks = defaultdict(list)
        self.freq = defaultdict(int)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.stacks[self.freq[val]].append(val)
        if self.freq[val] > self.max_freq:
            self.max_freq = self.freq[val]

    def pop(self) -> int:
        num = self.stacks[self.max_freq].pop()
        self.freq[num] -= 1
        if not self.stacks[self.max_freq]:
            self.max_freq -= 1
        return num