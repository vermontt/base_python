import pytest


def test_triangle_figure1(triangle_list):
    """Проверка методов вычисления периметра
     и площади для треугольника """
    assert triangle_list.__getitem__(0).perimeter() == 12
    assert triangle_list.__getitem__(0).area() == 6


def test_triangle_figure2(triangle_list):
    """Проверка метода сложения
     площадей нескольких треугольников """
    assert triangle_list.__getitem__(1) \
               .add_area(triangle_list.__getitem__(2)) == 24


def test_triangle_figure3(triangle_list):
    """Проверка возникновения исключения
     при попытке сложить площадь фигуры
      с челочисленным значением"""
    with pytest.raises(ValueError):
        triangle_list.__getitem__(3).add_area(44)
