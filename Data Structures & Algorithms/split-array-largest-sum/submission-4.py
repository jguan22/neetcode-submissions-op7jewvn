class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # binary search the sum: O(NlogS)
        l, r = max(nums), sum(nums)

        # helper to see if given sum is valid: O(N)
        def splitArray(n):
            curr_sum = 0
            split = 1
            for num in nums:
                if curr_sum + num > n:
                    curr_sum = num
                    split += 1
                else:
                    curr_sum += num
            return split

        # binary search: O(logS), where S is total sum
        while l < r:
            mid = (l + r) // 2
            if splitArray(mid) > k:
                l = mid + 1
            else:
                r = mid
        
        return l