class MinStack:
    # need to track each min of the remaining elements

    def __init__(self):
        # for each element, store curr min: (num, curr_min)
        self.stack = []

    def push(self, val: int) -> None:
        curr_min = val
        if self.stack and self.stack[-1][1] < curr_min:
            curr_min = self.stack[-1][1]

        self.stack.append((val, curr_min))

    def pop(self) -> None:
        val, _ = self.stack.pop()
        return val

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
