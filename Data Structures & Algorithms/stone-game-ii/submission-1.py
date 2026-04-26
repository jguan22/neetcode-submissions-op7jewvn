class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # precompute suffix sum for fast query
        n = len(piles)
        suffix_sum = [0] * (n+1)
        for i in range(n-1, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + piles[i]

        dp = {}

        def dfs(start, M):
            # take all stones if we can
            if start + 2 * M >= n:
                return suffix_sum[start]
            
            if (start, M) in dp:
                return dp[(start, M)]
            
            max_take = 0
            for X in range(1, 2*M+1):
                opponent_take = dfs(start + X, max(X, M))
                max_take = max(max_take, suffix_sum[start] - opponent_take)
            
            dp[(start, M)] = max_take
            return max_take
        
        return dfs(0, 1)