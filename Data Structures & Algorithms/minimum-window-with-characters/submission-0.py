class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sanity check
        n1 = len(s)
        n2 = len(t)
        if n1 < n2:
            return ""

        # build the freq_map of t
        freq_t = defaultdict(int)
        for c in t:
            freq_t[c] += 1
        unique = len(freq_t)

        # use sliding window
        l, r = 0, 0
        freq_s = defaultdict(int)
        checked = 0
        min_len = float('inf')
        start = -1

        # expand the window to see if any possible ans
        while r < n1:
            freq_s[s[r]] += 1
            
            # increment checked if number matches
            if freq_s[s[r]] == freq_t[s[r]]:
                checked += 1
                
                # once a valid answer appears, shrink the window
                while checked == unique:
                    # record the smallest valid window
                    if r-l+1< min_len:
                        start = l
                        min_len = r-l+1

                    # move the l forward until it's invalid
                    freq_s[s[l]] -= 1
                    if freq_s[s[l]] < freq_t[s[l]]:
                        checked -= 1
                    l += 1

            # increment r    
            r += 1
        
        return s[start:start+min_len] if start != -1 else ""