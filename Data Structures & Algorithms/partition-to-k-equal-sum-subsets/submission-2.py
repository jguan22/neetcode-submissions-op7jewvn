class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # sanity check
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        subsets = [0] * k
        nums.sort(reverse=True)
        n = len(nums)

        def backtrack(i):
            # base case
            if i >= n:
                return True
            
            # try all possible subsets
            for j in range(k):
                if subsets[j] + nums[i] <= target:
                    # skip duplicates
                    if j > 0 and subsets[j] == subsets[j - 1]:
                        continue

                    subsets[j] += nums[i]
                    if backtrack(i + 1):    # any true combination works
                        return True

                    # backtrack
                    subsets[j] -= nums[i]
                elif subsets[j] == 0:
                    # immediate false if any num larger than target
                    return False

            return False
        
        return backtrack(0)