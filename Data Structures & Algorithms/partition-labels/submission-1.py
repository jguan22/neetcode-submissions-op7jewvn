class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        queue = deque()
        start = 0
        ans = []
        n = len(s)
        while start < n:
            queue.append(s[start])
            i = start

            while queue:
                c = queue.popleft()

                # keep going until we have all c
                while count[c] != 0 and i < n:
                    count[s[i]] -= 1
                    queue.append(s[i])
                    i += 1
            
            ans.append(i-start)
            start = i

        return ans