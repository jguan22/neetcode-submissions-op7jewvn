class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # square needs all four edges with same length
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        edge = total // 4
        n = len(matchsticks)
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        # place match one by one, place the longer ones first
        def backtrack(i):
            if i == n:
                return True

            for side in range(4):
                if sides[side] + matchsticks[i] <= edge:
                    sides[side] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[side] -= matchsticks[i]
                
                # if match cant be placed into an empty side, false right away
                if sides[side] == 0:
                    break

            return False
        
        return backtrack(0)