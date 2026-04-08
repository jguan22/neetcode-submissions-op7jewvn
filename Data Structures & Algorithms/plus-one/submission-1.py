class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)
        for i in range(n-1, -1, -1):
            curr_sum = digits[i] + carry
            digits[i] = curr_sum % 10
            carry = curr_sum // 10
            if carry == 0:
                break
        
        if carry == 1:
            digits.insert(0, carry)
        
        return digits