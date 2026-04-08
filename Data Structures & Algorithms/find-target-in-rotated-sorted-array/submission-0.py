class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the smallest num
        lo = 0
        n = len(nums)
        hi = n - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] <= nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        
        offset = lo
        lo = 0
        hi = n - 1
        # find the number
        while lo < hi:
            # convert the index
            mid = (lo + hi) // 2
            real_mid = (mid + offset) % n

            if nums[real_mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        
        index = (lo + offset) % n
        return index if nums[index] == target else -1