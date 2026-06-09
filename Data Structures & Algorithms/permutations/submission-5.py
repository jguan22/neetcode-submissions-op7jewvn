class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # use swapping solution to save space complexity
        n = len(nums)
        ans = []

        def backtrack(start):
            # base case
            if start >= n:
                ans.append(nums[:])
                return
            
            for i in range(start, n):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start + 1)
                nums[i], nums[start] = nums[start], nums[i]
        
        backtrack(0)
        return ans

        '''
        n = len(nums)
        ans = []
        curr_list = []
        visited = [False] * n

        def backtrack():
            # base case
            if len(curr_list) == n:
                ans.append(curr_list[:])
                return
            
            for i in range(n):
                if visited[i]:
                    continue
                
                curr_list.append(nums[i])
                visited[i] = True
                backtrack()

                curr_list.pop()
                visited[i] = False

        backtrack()
        return ans
        '''