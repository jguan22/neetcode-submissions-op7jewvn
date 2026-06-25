class Solution:
    def numSquares(self, n: int) -> int:
        # precompute the squares list O(sqr(n))
        squares = []
        for i in range(1, n+1):
            if i * i > n:
                break
            squares.append(i*i)
        
        # dp: sum to n O(n * sqr(n))
        dp = [float('inf')] * (n + 1)
        dp[0] = 0   # base case
        for i in range(1, n+1):
            for num in squares:
                if num > i:
                    break

                dp[i] = min(dp[i], dp[i - num] + 1)
        
        return dp[n]