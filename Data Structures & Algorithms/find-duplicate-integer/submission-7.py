class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # to use O(1) space: use slow, fast pointer to find cycle
        slow = fast = 0

        # first, find the loop: O(n)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # then, find the start of the loop (duplicate num): O(n)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow