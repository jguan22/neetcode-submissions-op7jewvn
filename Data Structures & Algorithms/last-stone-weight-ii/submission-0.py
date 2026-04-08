class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # basically adding +/- for each num to minimize the sum
        total = sum(stones)
        n = len(stones)
        dp = [[False] * (2*total+1) for _ in range(n)]
        # base case
        dp[0][total + stones[0]] = dp[0][total - stones[0]] = True

        for i in range(1, n):
            for j in range(2*total+1):
                if dp[i-1][j]:
                    dp[i][j + stones[i]] = dp[i][j - stones[i]] = True

        smallest = float('inf')
        for j in range(2*total+1):
            if dp[n-1][j]:
                smallest = min(smallest, abs(j - total))
        return smallest