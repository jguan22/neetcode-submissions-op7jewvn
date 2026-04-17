class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        permutations = []
        visited = [False] * n

        def backtrack(curr):
            if len(curr) == n:
                permutations.append(curr[:])
                return
            
            for i in range(n):
                if visited[i]:
                    continue
                
                visited[i] = True
                curr.append(nums[i])
                backtrack(curr)
                curr.pop()
                visited[i] = False
        
        backtrack([])
        return permutations