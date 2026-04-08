class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * (n + 1)
        dp[n] = 0  # No stones left = 0 score

        for i in range(n - 1, -1, -1):
            take = 0
            # can take 1, 2, or 3 stones
            for j in range(i, min(i + 3, n)):
                take += stoneValue[j]
                # Relative lead = current stones - opponent's best lead
                dp[i] = max(dp[i], take - dp[j + 1])

        if dp[0] == 0:
            return "Tie"
        return  "Alice" if dp[0] > 0 else "Bob"