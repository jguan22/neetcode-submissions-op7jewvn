class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        available = set([0])

        for i in range(n):
            if i not in available:
                continue
            
            for j in range(i+minJump, i+maxJump+1):
                if j < n and s[j] == '0':
                    available.add(j)
                
        return n-1 in available