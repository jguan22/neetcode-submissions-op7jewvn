class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # binary search the minimized largest sum
        # the lower bound of answer is largest num in list
        # the higher bound is the total sum
        l, r = max(nums), sum(nums)

        # helper method to check if num is valid
        def isValid(num):
            currSum = 0
            group = 0
            for n in nums:
                # add number to curr subgroup until max is reached
                if currSum + n <= num:
                    currSum += n
                else:
                    currSum = n
                    group += 1
            
            return group < k


        while l < r:
            mid = l + (r-l) // 2
            # find the smallest possible num which is valid
            if isValid(mid):
                r = mid
            else:
                l = mid + 1

        return l