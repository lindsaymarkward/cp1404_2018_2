# Code Listing 11.7

import math  # need sqrt (square root)


class Point(object):
    """A Cartesian point (x, y) - all values are floats unless otherwise stated."""

    def __init__(self, x=0.0, y=0.0):
        """Initialise a point with x and y coordinates."""
        self.x = x
        self.y = y

    def distance(self, other):
        """Get the distance between self and another Point."""
        x_diff = self.x - other.x  # (x1 — x2)
        y_diff = self.y - other.y  # (y1 — y2)
        # square differences, sum, and take sqrt
        return math.sqrt(x_diff ** 2 + y_diff ** 2)

    def sum(self, other):
        """Vector Sum of self and a Point, return a Point instance."""
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        """Print a Point as a coordinate pair."""
        return "({:.2f}, {:.2f})".format(self.x, self.y)
