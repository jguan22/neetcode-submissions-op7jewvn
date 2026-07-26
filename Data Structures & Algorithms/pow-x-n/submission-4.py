class Solution:
    def myPow(self, x: float, n: int) -> float:
        # perform the process in a binary manner: O(logn)
        # base case:
        if n == 0:
            return 1
        
        if n == 1:
            return x
        
        # negative case:
        if n < 0:
            x = 1 / x
            n = -n
        
        if n % 2 == 1:
            return x * self.myPow(x * x, n // 2)
        else:
            return self.myPow(x * x, n // 2)