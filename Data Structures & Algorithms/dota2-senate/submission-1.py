class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_que = deque([i for i, s in enumerate(senate) if s == 'R'])
        d_que = deque([i for i, s in enumerate(senate) if s == 'D'])
        n = len(senate)
        
        while r_que and d_que:
            r, d = r_que.popleft(), d_que.popleft()
            if r < d: # Radiant bans Dire
                r_que.append(r + n)
            else:     # Dire bans Radiant
                d_que.append(d + n)
                
        return "Radiant" if r_que else "Dire"