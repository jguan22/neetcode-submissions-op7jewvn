class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if n > m:
            return ""

        freq_map = Counter(t)
        target = len(freq_map)
        l = 0
        min_len = float('inf')
        start = 0
        for r in range(m):
            freq_map[s[r]] -= 1
            if freq_map[s[r]] == 0:
                target -= 1
            
            while target == 0:
                if r-l+1 < min_len:
                    start = l
                    min_len = r-l+1
                    
                freq_map[s[l]] += 1
                if freq_map[s[l]] == 1:
                    target += 1
                l += 1
        
        return s[start:start+min_len] if min_len != float('inf') else ""