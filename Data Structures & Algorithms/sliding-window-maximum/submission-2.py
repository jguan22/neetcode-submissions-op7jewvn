class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # decreasing queue
        queue = deque()
        res = []
        l = 0
        for r in range(len(nums)):
            while queue and queue[-1] < nums[r]:
                queue.pop()
            queue.append(nums[r])

            if r + 1 >= k:
                res.append(queue[0])

                if nums[l] == queue[0]:
                    queue.popleft()
                l += 1

        return res