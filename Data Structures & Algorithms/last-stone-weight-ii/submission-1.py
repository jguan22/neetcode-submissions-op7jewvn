class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)
        dp = [[False] * (2 * total + 1) for _ in range(n)]
        dp[0][total + stones[0]] = True
        dp[0][total - stones[0]] = True

        for i in range(1, n):
            for j in range(2 * total + 1):
                if dp[i - 1][j] == True:
                    dp[i][j + stones[i]] = True
                    dp[i][j - stones[i]] = True

        smallest = float('inf')
        for j in range(2*total+1):
            if dp[n-1][j]:
                smallest = min(smallest, abs(j - total))
        return smallest