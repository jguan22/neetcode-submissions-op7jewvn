class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort the list to easily avoid duplicate later
        nums.sort()
        n = len(nums)
        res = []
        subset = []
        
        def backtrack(i):
            if i >= n:
                res.append(subset[:])
                return
            
            # either include or skip
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

            # skip duplicates
            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1)
        
        backtrack(0)
        return res