class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        permutations = []
        seen = [False] * n

        def backtrack(curr):
            if len(curr) == n:
                permutations.append(curr[:])
                return
            
            for i in range(n):
                if seen[i]:
                    continue
                
                # skip duplicates when curr num is the same as last one and last one is skipped
                if i > 0 and nums[i] == nums[i-1] and not seen[i-1]:
                    continue
                
                curr.append(nums[i])
                seen[i] = True
                backtrack(curr)
                seen[i] = False
                curr.pop()
        
        backtrack([])
        return permutations