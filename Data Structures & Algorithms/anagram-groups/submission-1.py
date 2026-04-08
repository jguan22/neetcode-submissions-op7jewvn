class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        for string in strs:
            count = 26 * [0]
            for c in string:
                count[ord(c)-ord('a')] += 1
            
            key = tuple(count)
            str_map[key].append(string)

        return list(str_map.values())
