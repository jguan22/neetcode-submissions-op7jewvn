class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        target_dict = {}
        for i, num in enumerate(numbers):
            if num in target_dict:
                return [target_dict[num], i + 1]
            
            diff = target - num
            target_dict[diff] = i + 1
        return None
        