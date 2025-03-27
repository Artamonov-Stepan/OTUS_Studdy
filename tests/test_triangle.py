from src.circle import Circle
from src.triangle import Triangle
import pytest

@pytest.mark.parametrize("side_a, side_b, side_c", [
        (3, 4, 5),
])
def test_valid_triangle_creation(side_a, side_b, side_c):
    t = Triangle(side_a, side_b, side_c)
    assert t.side_a == side_a
    assert t.side_b == side_b
    assert t.side_c == side_c,f"Ожидаем что треугольник создастся"

@pytest.mark.parametrize("side_a, side_b, side_c, expected_area" , [
        (3, 4, 5, 6.0),
])
def test_square_area_positive_integer(side_a, side_b, side_c, expected_area):
    t = Triangle(side_a, side_b, side_c)
    assert t.area == expected_area, f"Ожидаем площадь равную {expected_area}"

@pytest.mark.parametrize("side_a, side_b, side_c, expected_perimeter" , [
        (3, 4, 5, 12),
])
def test_triangle_perimeter_positive_integer(side_a, side_b, side_c, expected_perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == expected_perimeter,f"Ожидаем периметр равный {expected_perimeter}"

@pytest.mark.parametrize('side_a, side_b, side_c, radius, expected_add_area',[
    (3, 4, 5, 5, 84.5),
])
def test_positive_add_area_with_other_figure(side_a, side_b, side_c, radius, expected_add_area):
    t = Triangle(side_a, side_b, side_c)
    c = Circle(radius)
    assert expected_add_area == round((t.area + c.area), 1), f"Ожидаем сумму площадей равную {expected_add_area}"

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