class Shape():
    def __init__(self):
        self.area = 0
    def area(self):
        return self.area
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.string = length
    def area(self):
        self.area = self.length * self.length
        return self.area