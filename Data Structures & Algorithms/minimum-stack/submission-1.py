class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        # keep the updated min with curr num (curr, currMin)
        if self.stack:
            currMin = min(self.stack[-1][1], val)
        else:
            currMin = val
        self.stack.append((val, currMin))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]


    def getMin(self) -> int:
        return self.stack[-1][1]
        
