class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use sorted lists: O(nlogn + mlogm)
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t