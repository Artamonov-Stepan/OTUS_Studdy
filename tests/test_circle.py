from src.figure import Figure
from src.circle import Circle
import math
import pytest


def test_circle_area_positive_integer():
    c = Circle(5)
    assert c.area == 78.5,f"Ожидаем площадь равную {round(math.pi * (5**2), 1)}"

def test_circle_perimeter_positive_integer():
    c = Circle(5)
    assert c.perimeter == 31.4,f"Ожидаем периметр равный {round(((5 * math.pi) * 2), 1)}"

# def test_add_area_with_other_figure():
#     c = Circle(25)
#     f = Figure(15)
#     assert c.add_area(f) == 25 + 15,f"Ожидаем сумму площадей равную {25 + 15}"

@pytest.mark.parametrize('radius, expected_exception',
                         [(5.5, ValueError),
                          (-5, ValueError),
                          (0, ValueError)],
                         ids=['float', 'minus', 'zero'])
def test_circle_area_negative_tests(radius, expected_exception):
    with pytest.raises(expected_exception):
        c = Circle(radius)
        c.area


@pytest.mark.parametrize('radius, expected_exception',
                         [(5.5, ValueError),
                          (-5, ValueError),
                          (0, ValueError)],
                         ids=['float', 'minus', 'zero'])
def test_circle_perimeter_negative_tests(radius, expected_exception):
    with pytest.raises(expected_exception):
        c = Circle(radius)
        c.perimeter