class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use hash set: O(n)
        unique = set()
        for num in nums:
            if num in unique:
                return True
            
            unique.add(num)
        
        return False