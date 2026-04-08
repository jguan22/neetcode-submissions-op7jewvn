class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # use sliding window
        l = 0
        freq_map = defaultdict(int)
        max_size = 0

        # keep tracking number of the most repeating char so far
        most_repeat = 0

        for r in range(len(s)):
            # move the right forward and update the map and number
            freq_map[s[r]] += 1
            most_repeat = max(most_repeat, freq_map[s[r]])

            # if window is invalid, window size - most_repeat > k
            if (r-l+1) - most_repeat > k:
                # move left
                freq_map[s[l]] -= 1
                l += 1

            # update max_size for valid windows
            max_size = max(max_size, r-l+1)

        return max_size