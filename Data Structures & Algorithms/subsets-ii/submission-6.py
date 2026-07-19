class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # backtracking 2^n states: O(n * 2^n)
        # sort the list for duplicates skipping purpose
        nums.sort()
        n = len(nums)
        res = []
        curr = []

        def backtrack(i):
            # base case: O(n)
            if i == n:
                res.append(curr[:])
                return
            
            # 1. add curr num
            curr.append(nums[i])
            backtrack(i+1)

            # 2. skip curr num
            curr.pop()

            # skip duplicates if num has been skipped
            while i < n-1 and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)
        
        backtrack(0)
        return res
