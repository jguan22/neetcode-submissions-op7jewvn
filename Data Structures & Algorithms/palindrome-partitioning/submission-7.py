class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # pre-compute all palindrome
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for l in range(n-1, -1, -1):
            for r in range(l, n):
                if s[l] == s[r]:
                    # single char or two chars
                    if l + 1 >= r:
                        dp[l][r] = True
                    else:
                        dp[l][r] = dp[l + 1][r - 1]
                
        ans = []
        curr_combi = []

        def backtrack(start):
            if start == n:
                ans.append(curr_combi[:])
                return
            
            for i in range(start, n):
                # find a palindrome, use it
                if dp[start][i]:
                    curr_combi.append(s[start:i+1])
                    backtrack(i+1)
                    curr_combi.pop()
        
        backtrack(0)
        return ans