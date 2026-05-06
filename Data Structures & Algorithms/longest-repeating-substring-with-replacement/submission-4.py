class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window: keep track on the freq within the window
        # the longest is max_fraq + k, shrink the window if necessary
        freq_map = defaultdict(int)
        max_freq = 0
        l = 0
        
        for r in range(len(s)):
            # update right bound and max freq
            freq_map[s[r]] += 1
            max_freq = max(freq_map[s[r]], max_freq)

            # shrink the window when cant cover it with k replace
            if r - l + 1 - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1

        return r - l + 1