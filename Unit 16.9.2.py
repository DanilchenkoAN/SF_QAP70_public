class Figures:
    def __init__(self, name):
        self.name = name

class Rectangle(Figures):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
    def get_area_rectangle(self):
        return f'Площадь прямоугольника = {self.length * self.width}'
    def get_info_rectangle(self):
        return f'''
Информация о фигуре:
Название фигуры: {self.name}
Сторона "a" прямоугольника = {self.length}
Сторона "b" прямоугольника = {self.width}'''

rectangle = Rectangle('прямоугольник', 6, 4)
print(rectangle.get_info_rectangle())
print(rectangle.get_area_rectangle())
