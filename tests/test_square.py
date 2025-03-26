from src.figure import Figure
from src.square import Square
import pytest


def test_square_area_positive_integer():
    s = Square(5)
    assert s.area == 25, f"Ожидаем площадь равную {5 * 5}"

def test_square_perimeter_positive_integer():
    s = Square(5)
    assert s.perimeter == 20, f"Ожидаем периметр равную {5 * 4}"

# def test_add_area_with_other_figure():
#     s = Square(25)
#     f = Figure(15)
#     assert s.add_area(f) == 25 + 15, f"Ожидаем сумму площадей равную {25 + 15}"

@pytest.mark.parametrize('side_a, expected_exception',
                         [(5.5, ValueError),
                          (-5, ValueError),
                          (0, ValueError)],
                         ids=['float', 'minus', 'zero'])
def test_square_area_negative_tests(side_a, expected_exception):
    with pytest.raises(expected_exception):
        s = Square(side_a)
        s.area


@pytest.mark.parametrize('side_a, expected_exception',
                         [(5.5, ValueError),
                          (-5, ValueError),
                          (0, ValueError)],
                         ids=['float', 'minus', 'zero'])
def test_square_perimeter_negative_tests(side_a, expected_exception):
    with pytest.raises(expected_exception):
        s = Square(side_a)
        s.perimeter
