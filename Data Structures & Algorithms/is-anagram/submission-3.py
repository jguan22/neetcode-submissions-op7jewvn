class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if two strings have same length
        if len(s) != len(t):
            return False

        letter_dict = defaultdict(int)
        for char in s:
            letter_dict[char] += 1
        
        for char in t:
            letter_dict[char] -= 1
            if letter_dict[char] < 0:
                return False
        
        return True