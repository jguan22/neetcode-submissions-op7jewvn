class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # monostack: non-decreasing time to arrive target
        sorted_list = sorted(zip(position, speed), key=lambda x:x[0], reverse=True)
        stack = []
        for pos, s in sorted_list:
            t = (target - pos) / s
            # join the fleet
            if stack and t <= stack[-1]:
                continue

            stack.append(t)
        
        return len(stack)