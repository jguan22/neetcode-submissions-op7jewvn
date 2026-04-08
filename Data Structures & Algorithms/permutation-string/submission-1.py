class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False

        freqMap1 = Counter(s1)
        isMatch = len(freqMap1)
        l = 0
        for r in range(m):
            freqMap1[s2[r]] = freqMap1.get(s2[r], 0) - 1
            if freqMap1[s2[r]] == 0:
                isMatch -= 1
            
            if r-l+1 > n:
                freqMap1[s2[l]] += 1
                if freqMap1[s2[l]] == 1:
                    isMatch += 1
                l += 1
            
            if isMatch == 0:
                return True
            

        return False 