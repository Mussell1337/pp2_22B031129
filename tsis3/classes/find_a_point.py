class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def show(self):
        print(f"point, ({self.x} {self.y})")
    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
    def dist(self, sec_point):
        return ((self.x - sec_point.x)**2 + (self.y - sec_point.y)**2)**0.5