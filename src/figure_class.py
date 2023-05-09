class Figure:

    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def add_area(self, figure):
        if issubclass(type(figure), Figure):
            return self.area() + figure.area()
        else:
            raise ValueError('Нельзя сложить площади указанных объектов')
