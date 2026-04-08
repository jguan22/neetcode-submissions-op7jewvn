class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use the num as next pointer to num-th node
        # there must be a cycle if duplicate exists
        # the duplicate is the starting position of the cycle
        # use fast/slow pointer
        slow = fast = 0
        while 1:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        
        ans = 0
        while ans != slow:
            ans = nums[ans]
            slow = nums[slow]
        
        return ans