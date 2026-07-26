class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # only digit 9 will produce carry to next digit
        for i in range(len(digits)-1, -1, -1):
            # if not 9, no carry, we stop
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # otherwise, set to 0 and move on to next digit
            digits[i] = 0
        
        # if loop is over and still has carry, add a leading 1
        return [1] + digits