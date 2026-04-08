class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s, deleted):
            l, r = 0, len(s) - 1
            while l < r:
                # already delete one char before
                if s[l] != s[r] and deleted:
                    return False
                # either delete s[l] or s[r]
                elif s[l] != s[r] and not deleted:
                    return isPalindrome(s[l+1:r+1], True) or isPalindrome(s[l:r], True)
                else:
                    l += 1
                    r -= 1
            
            return True
        
        return isPalindrome(s, False)