from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Стороны квадрата не могут быть меньше или равны 0")
        if side_a != int:
            raise ValueError("Стороны должны быть целыми числами!")
        super().__init__(side_a, side_a)

    @property
    def get_area(self):
        return self.side_a**2

    @property
    def get_perimeter(self):
        return self.side_a * 4

    @property
    def add_area(self, other_figure):
        return self.get_area + other_figure.get_area
