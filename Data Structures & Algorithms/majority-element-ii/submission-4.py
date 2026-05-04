class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        candidate1 = None
        candidate2 = None
        vote1 = 0
        vote2 = 0

        for num in nums:
            if num == candidate1:
                vote1 += 1
            elif num == candidate2:
                vote2 += 1
            elif vote1 == 0:
                candidate1 = num
                vote1 = 1
            elif vote2 == 0:
                candidate2 = num
                vote2 = 1
            else:
                vote1 -= 1
                vote2 -= 1
        
        res = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > n / 3:
                res.append(c)
        return res