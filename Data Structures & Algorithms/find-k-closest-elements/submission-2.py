class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search the left bound, where x - arr[left] <= arr[left + k] - x
        n = len(arr)
        l, r = 0, n - k     # the last valid left bound is n - k

        while l < r:
            mid = (l + r) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        
        return arr[l:l+k]