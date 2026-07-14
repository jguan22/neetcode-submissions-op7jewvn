class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # sliding window with a queue that keeps decreasing order
        ans = []
        queue = deque()      # (num, index)
        l = 0

        # linear scan: O(n)
        for r, num in enumerate(nums):
            # pop any num smaller in stack
            while queue and queue[-1][0] <= num:
                queue.pop()

            # insert the num in stack
            queue.append((num, r))

            # once the size of wind is reached, record the max
            if (r - l + 1) == k:
                ans.append(queue[0][0])

                # move left bound and update max if necessary
                if queue[0][1] == l:
                    queue.popleft()
                l += 1
        
        return ans