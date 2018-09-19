# Code Listing 11.7

from math import sqrt


class Point:
    """A Cartesian point (x, y) - all values are floats unless otherwise stated."""

    def __init__(self, x=0.0, y=0.0):
        """Initialise a point with x and y coordinates."""
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance(self, other):
        """Get the distance between self and another Point."""
        x_diff = self.x - other.x  # (x1 — x2)
        y_diff = self.y - other.y  # (y1 — y2)
        # square differences, sum, and take sqrt
        return sqrt(x_diff ** 2 + y_diff ** 2)

    def sum(self, other):
        """Vector Sum of self and a Point, return a Point instance."""
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        """Print a Point as a coordinate pair."""
        return "({:.2f}, {:.2f})".format(self.x, self.y)


if __name__ == '__main__':
    here = Point(1, 2)
    there = Point(2, 3)
    print(here + there)
    if here == there:
        print("Same")
    else:
        print("Not")
