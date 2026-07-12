class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search the left bound: O(log(n-k) + k)
        # left bound range is from 0 to n-k: O(log(n-k))
        l, r = 0, len(arr) - k

        while l < r:
            mid = (l + r) // 2
            left, right = arr[mid], arr[mid+k]

            # 3 scenarios: entire range on the right of x, (x - left) < (right - x), move left
            # entire range on the left of x, (x - left) > (right - x), move right
            # x in the range: normal case
            if (x - left) > (right - x):
                l = mid + 1
            else:
                r = mid
        
        # slicing takes O(k)
        return arr[l:l+k]