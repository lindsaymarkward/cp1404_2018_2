from math import pi

from week_09.shape import Shape


class Circle(Shape):
    # def __init__(self, x=0, y=0, radius=1):
    #     super().__init__(x, y)
    #     self.radius = radius

    def __init__(self, radius=1, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius

    def __str__(self):
        return "{}, radius {}".format(super().__str__(), self.radius)

    def __len__(self):
        return self.radius * 2

    def __getitem__(self, item):
        if item == 0:
            return self.x
        return item

    def area(self):
        return self.radius ** 2 * pi


if __name__ == '__main__':
    c = Circle(x=3, y=4, z=-10, radius=5)
    # c = Circle(3, 4, 5)
    print(c)
    print(c.area())
    print(c.z)
    print(c[0])
