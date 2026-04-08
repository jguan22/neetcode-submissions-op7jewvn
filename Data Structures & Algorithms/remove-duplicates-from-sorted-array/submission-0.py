class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                dup.append(i)

        for i in range(len(dup)-1, -1, -1):
            nums.pop(dup[i])
        
        return len(nums)
            