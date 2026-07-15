class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # use stack to form fleet: store time to arrive and keep increasing order
        fleets = []

        # combine lists and sort it by position: O(nlogn)
        cars = sorted(zip(position, speed), reverse=True)

        # check cars starting from pos close to target: O(n)
        for pos, s in cars:
            t = (target - pos) / s

            # form new fleet when a car arrive target later, else join last fleet
            if not fleets or t > fleets[-1]:
                fleets.append(t)
        
        return len(fleets)
        