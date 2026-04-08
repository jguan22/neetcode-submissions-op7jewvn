class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        target = ""
        while columnNumber > 0:
            columnNumber -= 1
            digit_num = columnNumber % 26
            digit_letter = chr(ord('A') + digit_num)
            target = digit_letter + target
            
            columnNumber //= 26
        
        return target