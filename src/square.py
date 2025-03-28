from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        self.side_a = side_a
        if side_a <= 0:
            raise ValueError("Стороны квадрата не могут быть меньше или равны 0")
        if not isinstance(side_a, int):
            raise ValueError("Стороны должны быть целыми числами!")
        super().__init__(side_a, side_a)

    @property
    def area(self):
        return self.side_a ** 2

    @property
    def perimeter(self):
        return self.side_a * 4