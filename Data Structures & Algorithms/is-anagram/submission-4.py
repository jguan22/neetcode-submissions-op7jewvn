class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map_s = Counter(t)
        freq_map_t = Counter(s)

        return freq_map_s == freq_map_t