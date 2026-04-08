class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        max_len = 0

        for i in range(len(s)):
            if s[i] in seen:
                # update the len
                max_len = max(max_len, i-l)

                # move the left pointer until it's s[i]
                while l < i and s[l] != s[i]:
                    seen.remove(s[l])
                    l += 1
                seen.remove(s[l])
                l += 1
            # update the set
            seen.add(s[i])

        # update the len beofre return
        max_len = max(max_len, len(s)-l)
        return max_len
