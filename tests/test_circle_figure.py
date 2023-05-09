import pytest


def test_circle_figure1(circle_list):
    """Проверка методов вычисления периметра
         и площади для круга """
    assert circle_list.__getitem__(0).perimeter() == 56.548667764616276
    assert circle_list.__getitem__(0).area() == 254.46900494077323


def test_circle_figure2(circle_list):
    """Проверка метода сложения
         площадей нескольких окружностей """
    assert circle_list.__getitem__(1) \
               .add_area(circle_list.__getitem__(2)) == 128.80529879718154


def test_circle_figure3(circle_list):
    """Проверка возникновения исключения
         при попытке сложить площадь фигуры
          с челочисленным значением"""
    with pytest.raises(ValueError):
        circle_list.__getitem__(3).add_area(44)
