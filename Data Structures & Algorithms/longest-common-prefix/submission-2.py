class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # use binary search
        maxlen = min(len(s) for s in strs)
        l, r = 0, maxlen
        while l < r:
            mid = (l + r) // 2
            if self.isValidPrefix(strs, mid):
                l = mid + 1
            else:
                r = mid
        
        return strs[0][:l]


    def isValidPrefix(self, strs, index):
        prefix = strs[0][:index+1]
        for i in range(len(strs)):
            if not strs[i].startswith(prefix):
                return False
        return True