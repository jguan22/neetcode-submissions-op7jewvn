class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False

        # use one hash table of 26 chars: O(1)
        char_table = [0] * 26

        # linear scan the string: O(n)
        for i in range(len(s)):
            char_table[ord(s[i]) - ord('a')] += 1
            char_table[ord(t[i]) - ord('a')] -= 1
        
        # check the table: it should be all 0s if anagram: O(1)
        for count in char_table:
            if count != 0:
                return False
        return True

        '''
        # use sorted lists: O(nlogn)
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t
        '''