class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        seen = set(deadends)
        queue = deque([("0000", 0)])
        while queue:
            curr, step = queue.popleft()
            if curr in seen:
                continue
            
            if curr == target:
                return step

            seen.add(curr)
            
            for i in range(4):
                curr_digit = int(curr[i])
                for direction in [1, -1]:
                    nxt_digit = (curr_digit + direction + 10) % 10
                    nxt = curr[:i] + str(nxt_digit) + curr[i+1:]
                    queue.append((nxt, step + 1))
        
        return -1