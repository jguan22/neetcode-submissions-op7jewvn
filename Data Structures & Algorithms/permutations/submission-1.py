class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        permutation = []

        def backtrack():
            if len(permutation) == n:
                res.append(permutation[:])
                return
            
            for i in range(n):
                if nums[i] in permutation:
                    continue
                permutation.append(nums[i])
                backtrack()
                permutation.pop()
        
        backtrack()
        return res