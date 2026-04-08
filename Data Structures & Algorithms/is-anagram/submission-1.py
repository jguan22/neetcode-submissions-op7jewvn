class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        
        for char in t:
            if char not in freq:
                return False

            freq[char] -= 1
            if freq[char] < 0:
                return False
        
        return all(count == 0 for count in freq.values())