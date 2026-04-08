class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # detect a circle in this graph where nums[i] is the pointer
        # the start of the circle is the repeated num
        slow = fast = 0
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while 1:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        
        return slow