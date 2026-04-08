class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            # Shift to 0-indexed: A=0, B=1, ..., Z=25
            columnNumber -= 1
            remain = columnNumber % 26
            ans = chr(ord('A') + remain) + ans

            columnNumber //= 26
        
        return ans