class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # binary search the prefix length
        def isValid(prefix):
            for word in strs:
                if not word.startswith(prefix):
                    return False
            return True
        
        min_len = min(len(s) for s in strs)
        l, r = 0, min_len
        while l < r:
            mid = l + (r - l) // 2
            pref = strs[0][:mid+1]
            if isValid(pref):
                l = mid + 1
            else:
                r = mid
        
        return strs[0][:l]  