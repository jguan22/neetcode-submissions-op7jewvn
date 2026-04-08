class StockSpanner:

    def __init__(self):
        # monostack
        self.stack = []
        

    def next(self, price: int) -> int:
        total_count = 1
        while self.stack and price >= self.stack[-1][0]:
            _, count = self.stack.pop()
            total_count += count
        self.stack.append((price, total_count))
        return total_count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)