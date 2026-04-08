class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # arr is sorted, so find the window with size k and return the slice
        l, r = 0, len(arr) - k

        # binary search the left bound
        while l < r:
            mid = (l + r) // 2
            # left bound is the first val that closer than right bound + 1
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        
        return arr[l:l+k]