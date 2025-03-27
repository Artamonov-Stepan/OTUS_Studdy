import math
from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус не может быть меньше 0")
        if not radius == int:
            raise ValueError("Радиус должен быть целым числом!")
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius**2)

    @property
    def perimeter(self):
        return (self.radius * math.pi) * 2

    @property
    def add_area(self, other_figure):
        return self.get_area + other_figure.get_area


c = Circle(int(input()))
