class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # saninity check
        if len(s1) > len(s2):
            return False
        
        # build freq map of s1
        n1 = len(s1)
        freq_s1 = defaultdict(int)
        for c in s1:
            freq_s1[c] += 1

        # use slide window
        n2 = len(s2)
        l = 0
        freq_s2 = defaultdict(int)
        for r in range(n2):
            freq_s2[s2[r]] += 1

            # comparing freq map of s1 and s2
            while l <= r and freq_s2[s2[r]] > freq_s1[s2[r]]:
                # move l forward
                freq_s2[s2[l]] -= 1
                l += 1

            # check the length of window
            if r-l+1 == n1:
                return True
        
        return False
