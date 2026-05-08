class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # helper to split array by given sum n
        def split(n):
            curr_sum = 0
            count = 1
            for num in nums:
                if curr_sum + num <= n:
                    curr_sum += num
                else:
                    curr_sum = num
                    count += 1
            return count

        # binary search the ans
        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            if split(mid) > k:
                l = mid + 1
            else:
                r = mid
        
        return l