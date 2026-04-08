class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            word_freq = [0] * 26
            for c in word:
                index = ord(c) - ord('a')
                word_freq[index] += 1

            anagram_map[tuple(word_freq)].append(word)
        
        return list(anagram_map.values())
