from src.figure_class import Figure


class Square(Figure):

    def __init__(self, name, side):
        super().__init__(name)
        self.side = side
        if type(self.side) != int:
            raise ValueError('Такую фигуру создать нельзя')

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side
