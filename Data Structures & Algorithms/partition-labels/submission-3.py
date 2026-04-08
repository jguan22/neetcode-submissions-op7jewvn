class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq_map = Counter(s)
        ans = []
        l = 0
        unique = set()
        for r in range(len(s)):
            curr = s[r]
            unique.add(curr)

            freq_map[curr] -= 1
            if freq_map[curr] == 0:
                unique.remove(curr)

            if len(unique) == 0:
                ans.append(r - l + 1)
                l = r + 1
        
        return ans