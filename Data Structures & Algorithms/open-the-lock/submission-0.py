class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # bfs
        dead = set(deadends)
        if "0000" in dead:
            return -1

        # for each step, (combination, distance)
        queue = deque()
        queue.append(("0000", 0))
        visited = {"0000"}

        while queue:
            curr, dist = queue.popleft()
            if curr == target:
                return dist
            
            # four digits, each one has two direction
            for i in range(4):
                digit = int(curr[i])
                for nxt in (-1, 1):
                    new_digit = (digit + nxt) % 10
                    nxt_combi = curr[:i] + str(new_digit) + curr[i+1:]

                    if nxt_combi not in dead and nxt_combi not in visited:
                        visited.add(nxt_combi)
                        queue.append((nxt_combi, dist + 1))
        
        # run out of options
        return -1