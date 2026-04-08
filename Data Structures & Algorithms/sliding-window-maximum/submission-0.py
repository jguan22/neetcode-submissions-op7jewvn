class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use deque to track the window
        queue = deque()
        ans = []
        l = 0
        
        for r in range(len(nums)):
            # keep queue decreasing
            while queue and queue[-1] < nums[r]:
                queue.pop()
            queue.append(nums[r])

            # record the max number once window size reaches
            if r >= k-1:
                ans.append(queue[0])

                # move l and pop number
                if queue[0] == nums[l]:
                    queue.popleft()
                l += 1
        
        return ans