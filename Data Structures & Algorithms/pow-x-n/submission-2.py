class Solution:
    def myPow(self, x: float, n: int) -> float:
        # base case:
        if n == 0:
            return 1
            
        # negative case
        if n < 0:
            x = 1 / x
            return self.myPow(x, -n)
            
        # odd number
        if n % 2 == 1:
            return x * self.myPow(x * x, (n - 1) // 2)
        else:
            return self.myPow (x * x, n // 2)