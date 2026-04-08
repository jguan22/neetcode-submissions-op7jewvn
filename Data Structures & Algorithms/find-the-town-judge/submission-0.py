class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # One array to track the "Net Trust"
        trust_score = [0] * (n + 1)
        
        for person_a, person_b in trust:
            trust_score[person_a] -= 1
            trust_score[person_b] += 1
            
        for i in range(1, n + 1):
            # The judge must be trusted by everyone else (n-1)
            if trust_score[i] == n - 1:
                return i
                
        return -1