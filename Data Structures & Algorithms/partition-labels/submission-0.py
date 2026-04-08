class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_map = Counter(s)
        ans = []
        active = set()

        # need to ensure queue is empty before move on to next substring
        l = 0
        for r, c in enumerate(s):
            char_map[c] -= 1
            active.add(c)

            if char_map[c] == 0:
                active.remove(c)
            
            if not active:
                ans.append(r-l+1)
                l = r + 1
            
        return ans