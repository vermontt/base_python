from src.figure_class import Figure


class Rectangle(Figure):

    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
        if type(self.length) | type(self.width) != int:
            raise ValueError('Такую фигуру создать нельзя')

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
