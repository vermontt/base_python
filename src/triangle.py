from src.figure_class import Figure


class Triangle(Figure):

    def __init__(self, name, sideA, sideB, sideC):
        super().__init__(name)
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC
        if type(self.sideA) | type(self.sideB) | type(self.sideC) != int:
            raise ValueError('Такую фигуру создать нельзя')

    def area(self):
        return 0.5 * self.sideA * self.sideB

    def perimeter(self):
        return self.sideA + self.sideB + self.sideC
