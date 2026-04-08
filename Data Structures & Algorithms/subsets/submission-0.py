class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            n = len(ans)
            for i in range(n):
                new_subset = ans[i].copy()
                new_subset.append(num)
                ans.append(new_subset)
        
        return ans