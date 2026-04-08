class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalSum = sum(nums)
        if totalSum % k != 0:
            return False
        
        target  = totalSum // k
        n = len(nums)
        nums.sort(reverse=True)
        subsets = [0] * n

        def backtrack(i):
            if i >= n:
                return True
            
            for j in range(k):
                if subsets[j] + nums[i] <= target:
                    subsets[j] += nums[i]
                    if backtrack(i+1):
                        return True
                    subsets[j] -= nums[i]
                
                if subsets[j] == 0:
                    return False
            
            return False
        
        return backtrack(0)