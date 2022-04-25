import math

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return f'Площадь прямоугольника = {self.a * self.b}'

class Square:
    def __init__(self, a):
        self.a = a
    def get_area_square(self):
        return f'Площадь квадрата = {self.a**2}'

class Circle:
    def __init__(self, r=0, d=0, p=0):
        self.r = r
        self.d = d
        self.p = p
    def get_area_circle(self):
        if self.r:
            sr = math.pi * pow(self.r, 2)
            sr = float('{:.2f}'.format(sr))
            return f'Площадь круга с радиусом {self.r} = {sr}'
        elif self.d:
            sd = math.pi * (pow(self.d, 2))/4
            sd = float('{:.2f}'.format(sd))
            return f'Площадь крега с диаметром {self.d} = {sd}'
        elif self.p:
            sp = pow(self.p, 2) / (4 * math.pi)
            sp = float('{:.2f}'.format(sp))
            return f'Площадь круга с длинной окружности {self.p} = {sp}'
