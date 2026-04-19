class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_len = sum(matchsticks)
        if total_len % 4 != 0:
            return False
        
        target = total_len // 4
        sides = [0] * 4
        n = len(matchsticks)
        matchsticks.sort(reverse=True)
        
        def backtrack(i):
            if i >= n:
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= target:
                    if j > 0 and sides[j] == sides[j-1]:
                        continue
                
                    sides[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j] -= matchsticks[i]

                if sides[j] == 0:
                        break
                        
            return False

        return backtrack(0)