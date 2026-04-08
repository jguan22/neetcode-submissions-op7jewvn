class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i:j+1] in wordDict:
                    dp[i][j] = True
        
        combinations = []
        
        def dfs(start, curr_combi):
            if start == n:
                res = " ".join(curr_combi)
                combinations.append(res)
                return
            
            for end in range(start, n):
                if dp[start][end]:
                    curr_combi.append(s[start:end + 1])
                    dfs(end + 1, curr_combi)
                    curr_combi.pop()
        
        dfs(0, [])
        return combinations