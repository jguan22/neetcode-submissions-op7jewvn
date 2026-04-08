class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        for str in strs:
            key = [0] * 26
            for char in str:
                key[ord(char) - ord('a')] += 1
            str_map[tuple(key)].append(str)
        return list(str_map.values())