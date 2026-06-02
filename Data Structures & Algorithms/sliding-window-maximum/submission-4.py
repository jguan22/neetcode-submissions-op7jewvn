class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a queue with decreasing order
        queue = deque()
        max_list = []

        for i in range(len(nums)):
            # pop any smaller num ahead
            while queue and queue[-1][0] <= nums[i]:
                queue.pop()

            queue.append((nums[i], i))

            if i >= (k - 1):
                # shrink the window
                if queue[0][1] <= (i - k):
                    queue.popleft()

                # record the curr max
                max_list.append(queue[0][0])
        
        return max_list