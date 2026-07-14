class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # use a set to track what char in the window
        char_set = set()
        max_len = 0
        l = 0

        # linear scan: O(n)
        for r, c in enumerate(s):
            # char already exists, move l
            while c in char_set:
                char_set.remove(s[l])
                l += 1
            
            # add char and update max len
            char_set.add(c)
            max_len = max(max_len, (r - l + 1))

        return max_len