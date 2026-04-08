class CountSquares:

    def __init__(self):
        # need a dict to track the points and their freq
        self.points = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1


    def count(self, point: List[int]) -> int:
        px, py = point

        # need (px,py), (x, y), (x, py), (px, y) four points to form a square
        ans = 0
        for (x, y), count in self.points.items():
            if x == px and y == py:
                continue

            if abs(px-x) != abs(py-y):
                continue
            
            count1 = self.points.get((px, y), 0)
            count2 = self.points.get((x, py), 0)
            if count1 == 0 or count2 == 0:
                continue
            
            ans += count1 * count2 * count
        
        return ans
