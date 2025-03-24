from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Стороны прямоугольника не могут быть меньше или равны 0")
        if side_a or side_b != int:
            raise ValueError("Стороны должны быть целыми числами!")
        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2

    @property
    def add_area(self, other_figure):
        return self.get_area + other_figure.get_area


r = Rectangle(int(input()), int(input()))
