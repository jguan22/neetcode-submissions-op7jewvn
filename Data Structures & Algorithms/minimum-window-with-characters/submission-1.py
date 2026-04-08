class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window with dict
        m = len(s)
        n = len(t)
        res = ""
        if m < n:
            return res
        
        # use dict to track match of each char
        freqMap = Counter(t)
        numMatch = len(freqMap)

        l = r = 0
        minSize = float('inf')
        # move the right bound to find a substring
        while r < m:
            freqMap[s[r]] = freqMap.get(s[r], 0) - 1
            if freqMap[s[r]] == 0:
                numMatch -= 1

            # find all match substring
            while numMatch == 0 and l <= r:
                # update the size and result
                if (r-l+1) < minSize:
                    minSize = r-l+1
                    res = s[l:r+1]
                
                # shrink the window
                freqMap[s[l]] += 1
                if freqMap[s[l]] > 0:
                    numMatch += 1
                l += 1

            r += 1
        
        return res
