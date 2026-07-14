class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sanity check
        n, m = len(s1), len(s2)
        if n > m:
            return False

        # sliding window
        char_map = Counter(s1)
        l = 0

        for r in range(m):
            char_map[s2[r]] -= 1

            while char_map[s2[r]] < 0:
                char_map[s2[l]] += 1
                l += 1
            
            if r - l + 1 == n:
                return True
        
        return False