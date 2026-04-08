class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # use fixed size sliding window
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        
        freq_map = Counter(s1)
        num_match = len(freq_map)
        l = 0
        for r in range(m):
            freq_map[s2[r]] -= 1
            if freq_map[s2[r]] == 0:
                num_match -= 1
            
            if (r-l+1) > n:
                freq_map[s2[l]] += 1
                if freq_map[s2[l]] == 1:
                    num_match += 1
                l += 1
            
            if num_match == 0:
                return True
        
        return False