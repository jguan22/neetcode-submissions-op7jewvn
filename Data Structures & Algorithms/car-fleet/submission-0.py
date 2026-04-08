class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # need to check the car from the one closer to target
        # if car from behind can catch it, they form a fleet
        # the car in the front of a fleet must be the slowest one
        cars = []
        for i in range(len(position)):
            dis = target - position[i]
            time = dis / speed[i]
            cars.append((dis, time))
        
        cars.sort()
        stack = []
        for dis, time in cars:
            if stack and time <= stack[-1]:
                continue
            
            stack.append(time)
        
        return len(stack)