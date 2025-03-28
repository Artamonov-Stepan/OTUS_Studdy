from src.circle import Circle
from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    "side_a, side_b, expected_area",
    [
        (3, 5, 15),
    ],
)

def test_rectangle_area_positive_integer(side_a, side_b, expected_area):
    r = Rectangle(side_a, side_b)
    assert r.area == expected_area, f"Ожидаем площадь равную {expected_area}"

@pytest.mark.parametrize(
    "side_a, side_b, expected_perimeter",
    [
        (3, 5, 16),
    ],
)
def test_rectangle_perimeter_positive_integer(side_a, side_b, expected_perimeter):
    r = Rectangle(side_a, side_b)
    assert r.perimeter == expected_perimeter, (
        f"Ожидаем периметр равную {expected_perimeter}"
    )


@pytest.mark.parametrize(
    "radius, side_a, side_b, expected_add_area",
    [
        (5, 3, 5, 93.5),
    ],
)
def test_positive_add_area_with_other_figure(side_a, side_b, radius, expected_add_area):
    r = Rectangle(side_a, side_b)
    c = Circle(radius)
    assert expected_add_area == round((c.area + r.area), 1), (
        f"Ожидаем сумму площадей равную {expected_add_area}"
    )


@pytest.mark.parametrize(
    "side_a, side_b, expected_exception",
    [
        (3.5, 5.5, ValueError), (-1, 5, ValueError), (0, 5, ValueError)
    ],
    ids=["float", "minus", "zero"],
)

def test_rectangle_area_negative_tests(side_a, side_b, expected_exception):
    with pytest.raises(expected_exception):
        r = Rectangle(side_a, side_b)
        r.area


@pytest.mark.parametrize(
    "side_a, side_b, expected_exception",
    [(3.5, 5.5, ValueError), (-1, 5, ValueError), (0, 5, ValueError)],
    ids=["float", "minus", "zero"],
)

def test_rectangle_perimeter_negative_tests(side_a, side_b, expected_exception):
    with pytest.raises(expected_exception):
        r = Rectangle(side_a, side_b)
        r.perimeter

class NotAFigure:
       pass

@pytest.mark.parametrize("side_a, side_b, not_a_figure", [
    (3, 5, "Some_str"),
    (3, 5, 10),
    (3, 5, NotAFigure()),
])
def test_add_area_negative(side_a, side_b, not_a_figure):
    r = Rectangle(side_a, side_b)
    with pytest.raises(ValueError):
        r.add_area(not_a_figure)
