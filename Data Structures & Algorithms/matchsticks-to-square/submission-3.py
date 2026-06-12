class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # sanity check
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        target = total // 4
        n = len(matchsticks)
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def backtrack(i):
            # base case: use up all matchsticks to make sides as target length
            if i >= n:
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= target: 
                    # skip duplicates to save time
                    if j > 0 and sides[j] == sides[j-1]:
                        continue

                    # try each side and dfs each possible combination
                    sides[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True

                    # backtrack
                    sides[j] -= matchsticks[i]

                elif sides[j] == 0:
                    # immediate false if cant fit in an empty side
                    return False

            return False

        return backtrack(0)