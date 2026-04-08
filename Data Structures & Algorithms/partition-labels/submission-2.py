class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # pre-compute the last occurance of each char
        last = {c: i for i, c in enumerate(s)}
        ans = []
        start = end = 0
        n = len(s)
        for i in range(n):
            end = max(end, last[s[i]])
            if end == i:
                ans.append(end-start+1)
                start = end + 1
        
        return ans