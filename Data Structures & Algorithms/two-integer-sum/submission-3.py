class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a hash map to track all prev res to do one linear scan: O(n)
        target_map = {}

        for i, num in enumerate(nums):
            diff = target - num
            
            # check map if num exists
            if diff in target_map:
                return [target_map[diff], i]
            
            # record this num and index for later query
            target_map[num] = i

        return None