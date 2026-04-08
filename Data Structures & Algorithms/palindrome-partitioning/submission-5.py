class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        combinations = []

        # precompute the valid palindrome
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i < 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
        
        def dfs(start, combi):
            if start >= n:
                combinations.append(combi[:])
                return
            
            for end in range(start, n):
                if dp[start][end]:
                    combi.append(s[start:end+1])
                    dfs(end + 1, combi)
                    combi.pop()


        dfs(0, [])
        return combinations