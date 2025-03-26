from src.figure import Figure
from src.triangle import Triangle
import pytest

def test_valid_triangle_creation():
    t = Triangle(3, 4, 5)
    assert t.side_a == 3
    assert t.side_b == 4
    assert t.side_c == 5,f"Ожидаем что треугольник создастся"


def test_square_area_positive_integer():
    t = Triangle(3,4,5)
    assert t.area == 6.0, f"Ожидаем площадь равную 6.0"

def test_triangle_perimeter_positive_integer():
    t = Triangle(3, 4, 5)
    assert t.perimeter == 12,f"Ожидаем периметр равный 12"

# def test_add_area_with_other_figure():
#     t = Triangle(3, 4, 5)
#     f = Figure(15)
#     assert t.add_area(f) == 6.0 + 15,f"Ожидаем сумму площадей равную {6.0 + 15}"

@pytest.mark.parametrize('side_a, side_b, side_c, expected_exception',
                         [(1, 1, 3, ValueError),
                          (3, 4, 8, ValueError),
                          (7, 9, 17, ValueError)],
                         ids=['too_small_sum_1', 'too_small_sum_2', 'too_small_sum_3'])
def test_invalid_triangle_creation(side_a, side_b, side_c, expected_exception):
    with pytest.raises(expected_exception):
        Triangle(side_a, side_b, side_c)

@pytest.mark.parametrize('side_a, side_b, side_c, expected_exception',
                         [(3.5, 4.5, 5.5, ValueError),
                          (-3, -4, -5, ValueError),
                          (0, 0, 0, ValueError)],
                         ids=['float', 'minus', 'zero'])
def test_triangle_area_negative_tests(side_a, side_b, side_c, expected_exception):
    with pytest.raises(expected_exception):
        t = Triangle(side_a, side_b, side_c)
        t.area

@pytest.mark.parametrize('side_a, side_b, side_c, expected_exception',
                         [(3.5, 4.5, 5.5, ValueError),
                          (-3, -4, -5, ValueError),
                          (0, 0, 0, ValueError)],
                         ids=['float', 'minus', 'zero'])
def test_triangle_perimeter_negative_tests(side_a, side_b, side_c, expected_exception):
    with pytest.raises(expected_exception):
        t = Triangle(side_a, side_b, side_c)
        t.perimeter