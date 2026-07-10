class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        candidate1 = None
        candidate2 = None
        vote1 = 0
        vote2 = 0

        # loop through all nums: O(n)
        for num in nums:
            # increment vote if num is one of the candidates
            if num == candidate1:
                vote1 += 1
            elif num == candidate2:
                vote2 += 1
            # take one candidate spot if any available
            elif vote1 == 0:
                candidate1 = num
                vote1 = 1
            elif vote2 == 0:
                candidate2 = num
                vote2 = 1
            else:
                # decrement both if else
                vote1 -= 1
                vote2 -= 1
        
        # ensure cadidates are more than 1/3
        target = n / 3
        res = []
        for candidate in [candidate1, candidate2]:
            if nums.count(candidate) > target:
                res.append(candidate)
                
        return res