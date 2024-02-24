class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"
    
    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"
    
class Line:
    points = []

    def __init__(self, *points):
        self.points = list(points)

    def __add__(self, Point):
        self.points.append(Point)
        return self
    
    def __radd__(self, point):
        return self.__add__(point)
    
    def __len__(self):
        return len(self.points)
    
    def __getitem__(self, index):
        return self.points[index]
    
    def __setitem__(self, index, value):
        self.points[index] = value

p1 = Point(2, 8)
p2 = Point(1, 2)

l = Line(p1, p2)

p3 = Point(5, 6)

l[0] = p3

print(l[0])