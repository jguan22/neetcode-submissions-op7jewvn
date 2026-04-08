class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # binary search the answer
        def isValid(target_sum):
            num_array = 1
            curr_sum = 0
            for num in nums:
                if curr_sum + num > target_sum:
                    num_array += 1
                    curr_sum = num
                else:
                    curr_sum += num
            return num_array <= k
        
        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if isValid(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo