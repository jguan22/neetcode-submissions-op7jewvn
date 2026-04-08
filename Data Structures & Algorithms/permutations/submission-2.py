class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        seen = set()

        def dfs(permutation):
            if len(permutation) == n:
                ans.append(permutation[:])
                return
            
            for num in nums:
                if num in seen:
                    continue

                permutation.append(num)
                seen.add(num)
                dfs(permutation)

                # backtrack
                permutation.pop()
                seen.remove(num)
        
        dfs([])
        return ans