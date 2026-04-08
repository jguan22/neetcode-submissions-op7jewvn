class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        n = len(s)
        l = 0
        longest = 0
        freq = defaultdict(int)
        
        # keep the most freq char in the window
        mostFreq = 0
        for r in range(n):
            freq[s[r]] += 1
            mostFreq = max(mostFreq, freq[s[r]])

            # move the window if necessary
            # the most non_mostfreq char we can have is k
            while (r-l+1) - mostFreq > k:
                # not need to update mostFreq since max window wont increase
                freq[s[l]] -= 1
                l += 1
            
            longest = max(longest, (r-l+1))
        
        return longest