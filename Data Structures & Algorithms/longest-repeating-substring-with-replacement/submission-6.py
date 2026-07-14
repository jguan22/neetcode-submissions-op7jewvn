class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window: keep tracking the max freq of any char in the window
        freq_map = defaultdict(int)
        max_freq = 0
        l = 0
        
        # linear scan: O(n)
        for r in range(len(s)):
            freq_map[s[r]] += 1
            max_freq = max(max_freq, freq_map[s[r]])

            # move left bound if window_size - max_freq > k
            # meaning need to replace more than k chars
            if (r - l + 1) - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1
        
        return r - l + 1