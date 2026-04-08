class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        subset = []

        def backtrack(i):
            if i >= n:
                res.append(subset.copy())
                return
            
            # either include i-th num
            subset.append(nums[i])
            backtrack(i+1)

            # or skip it
            subset.pop()
            backtrack(i+1)
        
        backtrack(0)
        return res