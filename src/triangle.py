from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if (side_c >= side_a + side_b) or (side_a >= side_c + side_b) or (side_b >= side_a + side_c):
            raise ValueError(
                "С указанными сторонами треугольник создать нельзя, укажите другие значения сторон")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Стороны треугольника должны быть меньше или равны 0")
        if not isinstance(side_a, int) or not isinstance(side_b, int) or not isinstance(side_c, int):
            raise ValueError("Стороны должны быть целыми числами!")

    @property
    def area(self):
        p = ((self.side_a + self.side_b + self.side_c) / 2)
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
