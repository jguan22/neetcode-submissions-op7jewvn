class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # treat each i as a node and use nums[i] as next pointer
        # convert problem to looking for a circle in the list
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        target = 0
        while True:
            slow = nums[slow]
            target = nums[target]
            if slow == target:
                break
        
        return target