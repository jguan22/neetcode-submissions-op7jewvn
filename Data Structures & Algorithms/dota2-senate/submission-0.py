class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # the optimal way is always ban the next opponent
        # use queue and record the vote and member left
        queue = deque(senate)
        count_r = senate.count('R')
        count_d = senate.count('D')

        # vote > 0 means next D is baned, < 0 means R is baned
        vote = 0
        while count_r > 0 and count_d > 0:
            curr = queue.popleft()
            if curr == 'R':
                if vote < 0:
                    count_r -= 1
                else:
                    queue.append('R')
                vote += 1
            else:
                if vote > 0:
                    count_d -= 1
                else:
                    queue.append('D')
                vote -= 1
                
        return "Radiant" if count_r > 0 else "Dire"