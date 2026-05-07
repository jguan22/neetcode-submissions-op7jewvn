class MinStack:

    def __init__(self):
        # use a stack store (val, curr_min)
        self.stack = []

    def push(self, val: int) -> None:
        curr_min = val
        if self.stack and self.stack[-1][1] < val:
            curr_min = self.stack[-1][1]
        self.stack.append((val, curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
