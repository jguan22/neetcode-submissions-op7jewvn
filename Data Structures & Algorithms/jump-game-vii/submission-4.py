class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # sanity check: if last node cannot reach
        if s[-1] == '1':
            return False

        # bfs search: O(n)
        n = len(s)
        queue = deque([0])
        start = 0

        while queue:
            curr = queue.popleft()

            # base case
            if curr == n - 1:
                return True
            
            # try reachable range
            start = max(start, curr + minJump)  # skip nodes in queue already
            end = min(curr + maxJump, n - 1)
            for nxt in range(start, end+1):
                if s[nxt] == '0':
                    queue.append(nxt)
            
            start = end + 1
            
        
        return False