class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # binary search to find the peak
        # split the array into two, search the left and then right
        n = mountainArr.length()
        l, r = 0, n-1

        while l < r:
            mid = l + (r-l) // 2
            if mountainArr.get(mid) > mountainArr.get(mid+1):
                r = mid
            else:
                l = mid + 1
        
        peak = l

        # binary search left
        l, r = 0, peak
        while l < r:
            mid = l + (r-l) // 2
            if mountainArr.get(mid) >= target:
                r = mid
            else:
                l = mid + 1
        
        if mountainArr.get(l) == target:
            return l

        # binary search right
        l, r = peak, n-1
        while l < r:
            mid = l + (r-l) // 2
            if mountainArr.get(mid) > target:
                l = mid + 1
            else:
                r = mid
        
        return l if mountainArr.get(l) == target else -1