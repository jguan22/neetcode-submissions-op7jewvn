class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        total_sum = sum(nums)
        lo, hi = sum(nums) // k, sum(nums)

        def isValid(target_sum):
            count = 1
            curr_sum = 0
            for num in nums:
                if num > target_sum:
                    return False
                
                if num + curr_sum > target_sum:
                    curr_sum = num
                    count += 1
                else:
                    curr_sum += num
            
            return count <= k

        ans = hi
        while lo < hi:
            mid = (lo + hi) // 2
            if isValid(mid):
                hi = mid
                ans = min(ans, mid)
            else:
                lo = mid + 1
        return ans