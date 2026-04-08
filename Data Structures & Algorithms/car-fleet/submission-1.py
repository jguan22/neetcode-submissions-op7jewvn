class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # the slowest car become the front of the fleet
        # maintain a stack to mimic the formation of fleet
        # starting from the most front position
        zipped = zip(position, speed)
        cars = sorted(zipped, reverse=True)

        stack = []
        for pos, s in cars:
            t = (target - pos) / s

            # no car ahead or can never catch front car
            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)