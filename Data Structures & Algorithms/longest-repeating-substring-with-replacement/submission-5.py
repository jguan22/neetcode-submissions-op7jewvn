class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window: keep track on the freq of char in the window
        freq_map = defaultdict(int)
        max_freq = 0    # track on max freq
        l = 0

        # loop through string: O(n)
        for r in range(len(s)):
            freq_map[s[r]] += 1
            max_freq = max(max_freq, freq_map[s[r]])

            # keep window_size less than max_freq + k
            if (r - l + 1) > (max_freq + k):
                # move left bound
                freq_map[s[l]] -= 1
                l += 1

        # longest is not necessary max_freq + k, because may not use up all replacements
        return r - l + 1