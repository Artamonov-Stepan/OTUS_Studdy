from src.circle import Circle
from src.square import Square
import pytest

@pytest.mark.parametrize("side_a, expected_area", [
        (5, 25),
])
def test_square_area_positive_integer(side_a, expected_area):
    s = Square(side_a)
    assert s.area == expected_area, f"Ожидаем площадь равную {expected_area}"

@pytest.mark.parametrize("side_a, expected_perimeter", [
        (5, 20),
])
def test_square_perimeter_positive_integer(side_a, expected_perimeter):
    s = Square(side_a)
    assert s.perimeter == expected_perimeter, f"Ожидаем периметр равную {expected_perimeter}"

@pytest.mark.parametrize('radius, side_a, expected_add_area',[
    (5, 5, 103.5),
])
def test_positive_add_area_with_other_figure(side_a, radius, expected_add_area):
    s = Square(side_a)
    c = Circle(radius)
    assert expected_add_area == round((s.area + c.area), 1), f"Ожидаем сумму площадей равную {expected_add_area}"

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
#
# class NotAFigure:
#     # not_a_figure == other_figure # Из-за ошибки missing 1 required positional argument: 'other_figure'
#     #пытался прокинуть хоть какую-то связь, но это абстрактный параметр и не получается.
#     pass
#
# @pytest.mark.parametrize("radius, not_a_figure", [
#     (5, "Some_str"),
#     (5, 10),
#     (5, NotAFigure()),
# ])
# def test_add_area_negative(radius, not_a_figure):
#     c = Circle(radius)
#     with pytest.raises(ValueError):
#         c.add_area(not_a_figure)