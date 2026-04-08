class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window with dict
        m = len(s)
        n = len(t)
        if m < n:
            return ""
        
        # use dict to track match of each char
        freqMap = Counter(t)
        numMatch = len(freqMap)

        l = r = 0
        minSize = float('inf')
        start = -1
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
                    start = l
                
                # shrink the window
                freqMap[s[l]] += 1
                if freqMap[s[l]] > 0:
                    numMatch += 1
                l += 1

            r += 1
        
        return s[start:start+minSize] if minSize != float('inf') else ""