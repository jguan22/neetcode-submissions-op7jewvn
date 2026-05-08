class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # 1. locate the peak
        n = mountainArr.length()
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            # array has at least 3 num, thus mid + 1 is always a valid index
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        
        peak = l

        # 2. search left side
        l, r = 0, peak
        while l < r:
            mid = (l + r) // 2
            if mountainArr.get(mid) >= target:
                r = mid
            else:
                l = mid + 1
        
        if mountainArr.get(l) == target:
            return l
        
        # 3. search right side if target doesnot present in left
        l, r = peak, n - 1
        while l < r:
            mid = (l + r) // 2
            if mountainArr.get(mid) > target:
                l = mid + 1
            else:
                r = mid
        
        return l if mountainArr.get(l) == target else -1
                