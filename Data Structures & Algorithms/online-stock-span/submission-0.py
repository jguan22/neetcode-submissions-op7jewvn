class StockSpanner:

    def __init__(self):
        # use stack with strictly decreasing order (price, date)
        # only the price higher than any later day matters
        self.stack = []
        self.date = 0
        

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        
        if self.stack:
            # any higher price before, take diff
            res = self.date - self.stack[-1][1]
        else:
            # no higher price before, index + 1
            res = self.date + 1

        self.stack.append((price, self.date))
        self.date += 1

        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)