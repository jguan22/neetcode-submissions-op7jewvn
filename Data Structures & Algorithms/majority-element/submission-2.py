class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major_element = None
        major_count = 0
        for num in nums:
            if major_count == 0:
                major_element = num

            if num == major_element:
                major_count += 1
            else:
                major_count -= 1
        
        return major_element