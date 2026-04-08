class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            # base case:
            if n == 0:
                return 1
            
            # negative case
            if n < 0:
                x = 1 / x
                return helper(x, -n)
            
            # odd number
            nx = x * x
            if n % 2 == 1:
                return x * helper(nx, (n - 1) // 2)
            else:
                return helper(nx, n // 2)
        
        return helper(x, n)