class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        n = len(s)
        res = []
        curr = []


        def backtrack(start):
            if start >= n:
                res.append(" ".join(curr))
                return
            
            for i in range(start, n):
                if s[start:i+1] in wordSet:
                    curr.append(s[start:i+1])
                    backtrack(i+1)
                    curr.pop()
        
        backtrack(0)
        return res