import pytest


def test_square_figure1(square_list):
    """Проверка методов вычисления периметра
    и площади для квадрата """
    assert square_list.__getitem__(0).perimeter() == 12
    assert square_list.__getitem__(0).area() == 9


def test_square_figure2(square_list):
    """Проверка метода сложения
         площадей нескольких квадратов """
    assert square_list.__getitem__(1) \
               .add_area(square_list.__getitem__(2)) == 34


def test_square_figure3(square_list):
    """Проверка возникновения исключения
         при попытке сложить площадь фигуры
          с челочисленным значением"""
    with pytest.raises(ValueError):
        square_list.__getitem__(3).add_area(44)
