
# ? Method overriding is the process of rewritting the method inherited from the parent class

class Shape:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class Circle(Shape):
    def __init__(self, r):
        super().__init__(r, r)

    def area(self):
        return 3.14 * super().area()


cr = Circle(12)
print(cr.area())
