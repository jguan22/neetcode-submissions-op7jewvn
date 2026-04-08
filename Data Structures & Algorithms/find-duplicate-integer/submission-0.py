class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # treat nums list as a linked list where nums[i] is the next p
        # use fast slow pointers to find the cycle
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # use a another slow pointer to find the begin of the cycle
        slow2 = nums[0]

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow