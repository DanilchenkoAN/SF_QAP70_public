class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def get_to_string(self):
        return f'Rectanlge {self.x,  self.y, self.width, self.height}'

class Cilinder:
    def __init__(self, x, y, radius, height):
        self.x = x
        self.y = y
        self.radius = radius
        self.height = height
    def get_to_string(self):
        return f'Cilinder {self.x,  self.y, self.radius, self.height}'

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    def get_to_string(self):
        return f'Triangle {self.x1,  self.y1, self.x2, self.y2, self.x3, self.y3}'

rectangle = Rectangle(5,10,50,100)
print(rectangle.get_to_string())

cilinder = Cilinder(1,5,15,50)
print(cilinder.get_to_string())

triangle = Triangle(0, 0, 2, 2, 5, 0)
print(triangle.get_to_string())
