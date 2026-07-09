class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # it's easier to find subarrays with at most k elements
        # compute at most k and at most k - 1, and substract to get exact k

        # helper to find subarrays with at most n elements
        def atMost(n):
            # sliding window with a dict to track freq of chars
            l = 0
            freq_map = defaultdict(int)
            count = 0

            # loop through the list and move left bound in the loop: O(2n) -> O(n)
            for r in range(len(nums)):
                # check the num of elements
                if freq_map[nums[r]] == 0:
                    n -= 1
                freq_map[nums[r]] += 1

                # move left bound if too many int in the window
                while n < 0:
                    freq_map[nums[l]] -= 1
                    if freq_map[nums[l]] == 0:
                        n += 1

                    l += 1

                # update the num of subarrays with r as right bound
                count += (r - l + 1)
            
            return count
        
        return atMost(k) - atMost(k-1)