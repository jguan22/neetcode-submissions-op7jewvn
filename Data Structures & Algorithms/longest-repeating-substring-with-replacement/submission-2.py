class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        l = 0
        max_len = 0
        freq_map = defaultdict(int)
        max_freq = 1

        for r in range(len(s)):
            freq_map[s[r]] += 1
            max_freq = max(max_freq, freq_map[s[r]])

            if (r - l + 1) - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
            
        return max_len