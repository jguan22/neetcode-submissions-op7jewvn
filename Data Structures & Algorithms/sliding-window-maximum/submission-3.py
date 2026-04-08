class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a queue to track the max
        # and keep the queue in decreasing order
        queue = deque()
        l = 0
        ans = []
        for r in range(len(nums)):
            # pop smaller num in the queue
            while queue and nums[r] >= nums[queue[-1]]:
                queue.pop()
            queue.append(r)

            if r + 1 >= k:
                ans.append(nums[queue[0]])

                if queue[0] == l:
                    queue.popleft()
                l += 1

        return ans