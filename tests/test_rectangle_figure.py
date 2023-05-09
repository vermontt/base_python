import pytest


def test_rectangle_figure1(rectangle_list):
    """Проверка методов вычисления периметра
         и площади для прямоугольника """
    assert rectangle_list.__getitem__(0).perimeter() == 26
    assert rectangle_list.__getitem__(0).area() == 42


def test_rectangle_figure2(rectangle_list):
    """Проверка метода сложения
         площадей нескольких прямоугольников """
    assert rectangle_list.__getitem__(1)\
               .add_area(rectangle_list.__getitem__(2)) == 62


def test_rectangle_figure3(rectangle_list):
    """Проверка возникновения исключения
         при попытке сложить площадь фигуры
          с челочисленным значением"""
    with pytest.raises(ValueError):
        rectangle_list.__getitem__(3).add_area(44)
