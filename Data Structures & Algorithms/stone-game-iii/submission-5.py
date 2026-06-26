class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # dp bottom up to avoid max recursion
        n = len(stoneValue)
        dp = [0] * (n + 1)

        # n states and each has 3 takes O(n)
        for i in range(n-1, -1, -1):
            res = float('-inf')
            curr_take = 0
            for j in range(i, min(i + 3, n)):
                curr_take += stoneValue[j]
                res = max(res, curr_take - dp[j + 1])
            dp[i] = res
                
        if dp[0] > 0:  
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"