class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # sanity check
        if '0000' in deadends or target in deadends:
            return -1
        
        # bfs search
        queue = deque([('0000', 0)])
        seen = set(deadends)
        seen.add('0000')
        while queue:
            curr, step = queue.popleft()
            if curr == target:
                return step

            # iterate through 4 digits and 2 directions each
            for i in range(4):
                for direction in [1, -1]:
                    digit = str((int(curr[i]) + direction + 10) % 10)
                    nxt = curr[:i] + digit + curr[i+1:]
                    
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append((nxt, step + 1))
        
        return -1