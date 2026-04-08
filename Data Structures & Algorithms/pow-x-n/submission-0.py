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
            if n % 2 == 1:
                return x * helper(x * x, (n - 1) // 2)
            else:
                return helper(x * x, n // 2)
        
        return helper(x, n)