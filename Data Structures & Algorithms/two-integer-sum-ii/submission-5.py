class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers: make use of sorted order
        l, r = 1, len(numbers)

        # single pass: O(n)
        while l < r:
            curr_sum = numbers[l-1] + numbers[r-1]
            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                return [l, r]
        
        return None