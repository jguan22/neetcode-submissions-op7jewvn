class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sanity check
        n, m = len(s1), len(s2)
        if n > m:
            return False

        # sliding window: O(m + n)
        char_map = Counter(s1)
        l = 0

        for r in range(m):
            char_map[s2[r]] -= 1

            # move the left bound if too many of certain char in the window
            while char_map[s2[r]] < 0:
                char_map[s2[l]] += 1
                l += 1
            
            # find the permutation check
            if r - l + 1 == n:
                return True
        
        return False