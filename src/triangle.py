from src.figure import Figure

class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Стороны треугольника должны быть меньше или равны 0")
        if side_c >= side_a + side_b:
            raise ValueError(
                "С указанными сторонами треугольник создать нельзя, укажите другие значения сторон")
        if side_a or side_b or side_c != int:
            raise ValueError("Стороны должны быть целыми числами!")

    @property
    def area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0, 5

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def add_area(self, other_figure):
        return self.get_area + other_figure.get_area
t = Triangle(int(input()), int(input()), int(input()))

