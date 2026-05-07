class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # use stack to track the arriving time to keep an increasing order
        # because if a car from behind has smaller t, it will catch front car and form a fleet
        car_fleet = []
        cars = sorted(zip(position, speed), reverse=True)

        for pos, s in cars:
            # car with bigger t form a new fleet
            t = (target - pos) / s
            if car_fleet and car_fleet[-1] >= t:
                continue
            car_fleet.append(t)
        
        return len(car_fleet)