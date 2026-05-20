class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # precompute all subarrays for fast query
        n = len(piles)
        suffix_sum = [0] * (n+1)
        for i in range(n-1, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + piles[i]

        dp = {}

        def dfs(start, M):
            # base case: take all if possible
            if start + 2 * M >= n:
                return suffix_sum[start]
            
            # return prev explored route
            if (start, M) in dp:
                return dp[(start, M)]
            
            max_gain = 0
            for X in range(1, 2 * M + 1):
                curr_gain = suffix_sum[start] - dfs(start + X, max(M, X))
                max_gain = max(max_gain, curr_gain)
            
            dp[(start, M)] = max_gain
            return max_gain
        
        return dfs(0, 1)