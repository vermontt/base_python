import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.fixture()
def triangle_list():
    triangle1 = Triangle("Треугольник-1", 3, 4, 5)
    triangle2 = Triangle("Треугольник-2", 6, 7, 8)
    triangle3 = Triangle("Треугольник-3", 2, 3, 4)
    triangle4 = Triangle("Треугольник-4", 6, 7, 8)
    return triangle1, triangle2, triangle3, triangle4


@pytest.fixture()
def rectangle_list():
    rectangle1 = Rectangle("Прямоугольник-1", 6, 7)
    rectangle2 = Rectangle("Прямоугольник-2", 6, 7)
    rectangle3 = Rectangle("Прямоугольник-3", 4, 5)
    rectangle4 = Rectangle("Прямоугольник-4", 2, 3)
    return rectangle1, rectangle2, rectangle3, rectangle4


@pytest.fixture()
def circle_list():
    circle1 = Circle("Круг-1", 9)
    circle2 = Circle("Круг-2", 4)
    circle3 = Circle("Круг-3", 5)
    circle4 = Circle("Круг-4", 6)
    return circle1, circle2, circle3, circle4


@pytest.fixture()
def square_list():
    square1 = Square("Квадрат-1", 3)
    square2 = Square("Квадрат-2", 3)
    square3 = Square("Квадрат-3", 5)
    square4 = Square("Квадрат-4", 6)
    return square1, square2, square3, square4
