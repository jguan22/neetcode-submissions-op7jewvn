class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n-1] != '0': # sanity check
            return False

        queue = deque([0])
        checked = 0
        
        while queue:
            pos = queue.popleft()

            # next range to check, skip checked ones
            start = max(checked + 1, pos + minJump)
            end = min(n - 1, pos + maxJump)
            for i in range(start, end+1):
                if s[i] == '0':
                    if i == n - 1:
                        return True
                    queue.append(i)

            checked = max(checked, end)
            
        return False