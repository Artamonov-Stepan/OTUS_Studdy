from src.figure import Figure
from src.rectangle import Rectangle
from src.circle import Circle
import pytest


@pytest.mark.parametrize(
    "radius, expected_area",
    [
        (5, 78.5),
    ],
)
def test_circle_area_positive_integer(radius, expected_area):
    c = Circle(radius)
    assert c.area == expected_area, f"Ожидаем площадь равную {expected_area}"


@pytest.mark.parametrize(
    "radius, expected_perimeter",
    [
        (5, 31.4),
    ],
)
def test_circle_perimeter_positive_integer(radius, expected_perimeter):
    c = Circle(radius)
    assert round(c.perimeter, 1) == expected_perimeter, (
        f"Ожидаем периметр равный {expected_perimeter}"
    )


@pytest.mark.parametrize(
    "radius, side_a, side_b, expected_add_area",
    [
        (5, 3, 5, 93.5),
    ],
)
def test_positive_add_area_with_other_figure(radius, side_a, side_b, expected_add_area):
    c = Circle(radius)
    r = Rectangle(side_a, side_b)
    assert expected_add_area == round((c.area + r.area), 1), (
        f"Ожидаем сумму площадей равную {expected_add_area}"
    )


@pytest.mark.parametrize(
    "radius, expected_exception",
    [(5.5, ValueError), (-5, ValueError), (0, ValueError)],
    ids=["float", "minus", "zero"],
)
def test_circle_area_negative_tests(radius, expected_exception):
    with pytest.raises(expected_exception):
        c = Circle(radius)
        c.area


@pytest.mark.parametrize(
    "radius, expected_exception",
    [(5.5, ValueError), (-5, ValueError), (0, ValueError)],
    ids=["float", "minus", "zero"],
)
def test_circle_perimeter_negative_tests(radius, expected_exception):
    with pytest.raises(expected_exception):
        c = Circle(radius)
        c.perimeter


class NotAFigure:
        pass

@pytest.mark.parametrize("radius, not_a_figure", [
    (5, "Some_str"),
    (5, 10),
    (5, NotAFigure()),
])
def test_add_area_negative(radius, not_a_figure):
    c = Circle(radius)
    with pytest.raises(ValueError):
        c.add_area(not_a_figure)