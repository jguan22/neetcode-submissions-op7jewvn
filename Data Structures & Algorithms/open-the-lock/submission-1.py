class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"
        # edge case:
        if start in dead:
            return -1

        queue = deque([start])
        seen = {start}
        
        count = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                curr = queue.popleft()
                if curr == target:
                    return count

                # four digits
                for i in range(4):
                    digit = curr[i]
                    # two directions
                    for dir in (-1, 1):
                        nxt_digit = (int(digit) + dir) % 10
                        nxt_combi = curr[:i] + str(nxt_digit) + curr[i+1:]
                        if nxt_combi not in dead and nxt_combi not in seen:
                            seen.add(nxt_combi)
                            queue.append(nxt_combi)
            
            count += 1
            
        return -1