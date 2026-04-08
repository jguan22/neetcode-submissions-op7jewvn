class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # determine the offset of this array
        # by locate the smallest number
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        offset = l
        l, r = 0, n-1
        while l < r:
            mid = l + (r-l) // 2
            index = (mid + offset) % n
            if nums[index] >= target:
                r = mid
            else:
                l = mid + 1
        
        index = (l + offset) % n
        return index if nums[index] == target else -1