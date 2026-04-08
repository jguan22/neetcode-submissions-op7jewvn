class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort the list to easily avoid duplicate later
        nums.sort()
        n = len(nums)
        res = []
        subset = []
        
        def backtrack(start):
            res.append(subset[:])
            
            for i in range(start, n):
                # skip duplicate
                if i - start > 0 and nums[i] == nums[i-1]:
                    continue

                # either include or skip
                subset.append(nums[i])
                backtrack(i+1)
                subset.pop()
        
        backtrack(0)
        return res