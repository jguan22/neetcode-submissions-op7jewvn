class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # treat each i as a node and use nums[i] as next pointer
        # convert problem to looking for a circle in the list
        slow, fast = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        
        return slow