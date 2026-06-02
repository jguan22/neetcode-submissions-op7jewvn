class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search the left bound of range of k elements close to x
        l, r = 0, len(arr) - k   # the last possible pos of left bound

        while l < r:
            mid = (l + r) // 2
            left, right = arr[mid], arr[mid+k]

            # 3 possible scenario: x on the left, x in the middle, x on the right
            # either way it has the same condition
            if (x - left) > (right - x):
                l = mid + 1
            else:
                r = mid
        
        # left bound is closer or equal to right bound
        return arr[l:l+k]