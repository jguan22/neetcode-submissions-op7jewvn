class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        curr = []
        used = [False] * len(nums)

        def dfs():
            # base case
            if len(curr) == n:
                res.append(curr[:])
                return
            
            for i in range(n):
                # skip used ones
                if used[i]:
                    continue
                
                # skip duplicates (same char and last one was skipped)
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                curr.append(nums[i])
                used[i] = True
                dfs()
                used[i] = False
                curr.pop()
                

        dfs()
        return res