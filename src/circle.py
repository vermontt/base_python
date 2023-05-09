import math

from src.figure_class import Figure


class Circle(Figure):

    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        if type(self.radius) != int:
            raise ValueError('Такую фигуру создать нельзя')

    def area(self):
        return self.radius * self.radius * math.pi

    def perimeter(self):
        return 2 * self.radius * math.pi
