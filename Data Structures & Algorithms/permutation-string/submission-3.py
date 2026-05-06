class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window
        if len(s1) > len(s2):
            return False
        
        freq_map = Counter(s1)
        l = 0
        for r in range(len(s2)):
            # update freq map
            freq_map[s2[r]] -= 1

            # move left if necessary
            while freq_map[s2[r]] < 0:
                freq_map[s2[l]] += 1
                l += 1
            
            if r - l + 1 == len(s1):
                return True
                
        return False