class CountSquares:

    def __init__(self):
        # use a hash map for fast query
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point

        # loop through the list
        res = 0
        for (x, y), count in self.points.items():
            # only check the point on diagnol
            if px == x or py == y or abs(px - x) != abs(py - y):
                continue

            res += count * self.points.get((x, py), 0) * self.points.get((px, y), 0)

        return res