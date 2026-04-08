class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.rows = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
        self.rows[x].add(y)
        
    def count(self, point: List[int]) -> int:
        ox, oy = point
        total_count = 0
        for ny in self.rows[ox]:
            if ny == oy:
                continue

            # look for a square of (ox, oy), (ox, ny), (nx, oy), (nx, ny)
            count1 = self.points[(ox, ny)]
            side = abs(oy - ny)

            for nx in (ox + side, ox - side):
                count2 = self.points[(nx, oy)]
                count3 = self.points[(nx, ny)]
                total_count += count1 * count2 * count3

        return total_count
