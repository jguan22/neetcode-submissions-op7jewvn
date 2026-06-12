class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # precompute all possible partitions
        word_set = set(wordDict)
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i:j+1] in word_set:
                    dp[i][j] = True
                    
        combinations = []
        curr_list = []

        # helper to explore all possible combinations
        def backtrack(start):
            # base case
            if start >= n:
                combinations.append(" ".join(curr_list))
                return
            
            for end in range(start, n):
                if dp[start][end]:
                    curr_list.append(s[start:end+1])
                    backtrack(end+1)

                    # backtrack
                    curr_list.pop()
        
        backtrack(0)
        return combinations