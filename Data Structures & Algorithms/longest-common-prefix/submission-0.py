class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # use binary search
        maxlen = min(len(s) for s in strs)
        l, r = 0, maxlen
        while l < r:
            mid = (l + r) // 2
            if not self.isValidPrefix(strs, mid):
                r = mid
            else:
                l = mid + 1
        
        return strs[0][:l]


    def isValidPrefix(self, strs, index):
        prefix = strs[0][:index+1]
        for i in range(len(strs)):
            if prefix not in strs[i]:
                return False
        return True