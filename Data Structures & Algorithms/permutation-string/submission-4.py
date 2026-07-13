class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window
        # sanity check
        if len(s2) < len(s1):
            return False

        freq_map = Counter(s1)   # O(n)
        n = len(s1)
        l = 0

        # loop through s2 exact once: O(m)
        for r in range(len(s2)):
            freq_map[s2[r]] -= 1

            # move the left bound if too many of certain char in the window
            while freq_map[s2[r]] < 0:
                freq_map[s2[l]] += 1
                l += 1
            
            # find the permutation check
            if r - l + 1 == n:
                return True
        
        return False