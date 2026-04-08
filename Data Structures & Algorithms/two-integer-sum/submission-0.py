class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = defaultdict(int)
        for i, num in enumerate(nums):
            if num in diff:
                return [diff[num], i]

            difference = target - num
            diff[difference] = i

        return False