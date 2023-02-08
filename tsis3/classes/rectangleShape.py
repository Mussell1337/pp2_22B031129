class Shape():
    def __init__(self):
        self.area = 0
    def area(self):
        return self.area
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        self.area = self.length * self.width
        return self.area