class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer-Moore Voting Algorithm
        n = len(nums)
        target = n / 3
        vote1 = 0
        vote2 = 0
        num1 = num2 = 0

        # find two popular element
        for num in nums:
            if num == num1:
                vote1 += 1
            elif num == num2:
                vote2 += 1
            # Then check for EMPTY slots
            elif vote1 == 0:
                num1, vote1 = num, 1
            elif vote2 == 0:
                num2, vote2 = num, 1
            # Otherwise, decrement both (triple cancelation)
            else:
                vote1 -= 1
                vote2 -= 1
        
        # count exact freq of these two num
        vote1 = vote2 = 0
        for num in nums:
            if num == num1:
                vote1 += 1
            elif num == num2:
                vote2 += 1
        
        ans = []
        if vote1 > target:
            ans.append(num1)
        if vote2 > target:
            ans.append(num2)
        
        return ans