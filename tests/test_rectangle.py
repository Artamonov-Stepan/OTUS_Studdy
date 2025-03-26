from src.figure import Figure
from src.rectangle import Rectangle
import pytest


def test_rectangle_area_positive_integer():
    r = Rectangle(3,5)
    assert r.area == 15, f"Ожидаем площадь равную {3 * 5}"

def test_rectangle_perimeter_positive_integer():
    r = Rectangle(3,5)
    assert r.perimeter == 16, f"Ожидаем периметр равную {(3 + 5) * 2}"

# def test_add_area_with_different_figures():
#     r = Rectangle(3, 5)
#     f = Figure(10)
#     assert r.add_area(f) == 15 + 10, f"Ожидаем сумму площадей равную {15 + 10}"

@pytest.mark.parametrize('side_a, side_b, expected_exception',
                         [(3.5, 5.5, ValueError),
                          (-1, 5, ValueError),
                          (0, 5, ValueError)],
                         ids=['float', 'minus', 'zero'])
def test_rectangle_area_negative_tests(side_a, side_b, expected_exception):
    with pytest.raises(expected_exception):
        r = Rectangle(side_a, side_b)
        r.area


@pytest.mark.parametrize('side_a, side_b, expected_exception',
                         [(3.5, 5.5, ValueError),
                          (-1, 5, ValueError),
                          (0, 5, ValueError)],
                         ids=['float', 'minus', 'zero'])
def test_rectangle_perimeter_negative_tests(side_a, side_b, expected_exception):
    with pytest.raises(expected_exception):
        r = Rectangle(side_a, side_b)
        r.perimeter
