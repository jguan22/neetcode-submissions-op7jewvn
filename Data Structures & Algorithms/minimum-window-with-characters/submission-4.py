class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sanity check
        if len(s) < len(t):
            return ""

        # sliding window: count the unique chars in t and freq of each O(m + n)
        n, m = len(s), len(t)
        char_map = Counter(t)   # O(m)
        match = len(char_map)

        l = 0
        min_len = float('inf')
        ans = ""

        # linear scan: O(n)
        for r in range(n):
            # move the right bound until all chars are in the window
            char_map[s[r]] -= 1
            if char_map[s[r]] == 0:
                match -= 1

            # once all covered, try to move left bound
            while match == 0:
                # update min len
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    ans = s[l:l+min_len]
                
                # move left and update match
                char_map[s[l]] += 1
                if char_map[s[l]] > 0:
                    match += 1
                l += 1

        return ans