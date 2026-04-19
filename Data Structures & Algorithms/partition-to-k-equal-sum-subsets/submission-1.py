class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        target = total_sum // k
        
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        n = len(nums)
        subset_sum = [0] * k

        def backtrack(i):
            if i == n:
                return True
            
            for j in range(k):
                if subset_sum[j] + nums[i] <= target:
                    if j > 0 and subset_sum[j] == subset_sum[j-1]:
                        continue

                    subset_sum[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    subset_sum[j] -= nums[i]
            
            return False
        
        return backtrack(0)