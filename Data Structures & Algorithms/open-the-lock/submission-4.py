class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # sanity check
        if target in deadends or '0000' in deadends:
            return -1
        
        # bfs
        queue = deque([('0000', 0)])
        visited = set(deadends)
        visited.add('0000')

        while queue:
            curr_combi, step = queue.popleft()
            # base case:
            if curr_combi == target:
                return step

            for i in range(4):
                for move in [1, -1]:
                    # build the new number
                    new_digit = (int(curr_combi[i]) + move) % 10
                    new_combi = curr_combi[:i] + str(new_digit) + curr_combi[i+1:]

                    # add it to queue for later bfs
                    if new_combi not in visited:
                        visited.add(new_combi)
                        queue.append((new_combi, step + 1))

        return -1