class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # only care about the max value and values followed in the window
        # any smaller value on the left doesnt matter anymore
        # maintain a queue in a decreasing order
        queue = deque()
        l = 0
        ans = []
        for r in range(len(nums)):
            # pop any smaller value ahead
            while queue and queue[-1] < nums[r]:
                queue.pop()
            queue.append(nums[r])

            # add the head to ans when size reached
            if r + 1 >= k:
                ans.append(queue[0])

                # pop left
                if nums[l] == queue[0]:
                    queue.popleft()
                l += 1
            
        return ans