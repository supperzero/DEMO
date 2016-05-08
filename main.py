class Shapes():
    def __init__(self):
        self.area = 0

    def get_area(self):
        if self.area == 0:
            self.acumulate_area()
        print(self.area)
        return self.area

class Ellipse(Shapes):
    def __init__(self,a,b):
        self._a = a
        self._b = b
        self.area = 0
    def acumulate_area(self):
        self.area = 3.14 * self._a * self._b
        print(self.area)

class Square(Shapes):
    def __init__(self,a):
        self._a = a
        self.area = 0

    def acumulate_area(self):
        self.area = self._a * self._a

class Rectange(Shapes):
    def __init__(self,a,b):
        self._a = a
        self._b = b
        self.area = 0

    def acumulate_area(self):
        self.area = self._a * self._b

class Circle(Shapes):
    def __init__(self,a):
        self._a = a
        self.area = 0

    def acumulate_area(self):
        self.area = 3.14 * self._a * self._a


shapes = [Ellipse(10,20),Square(15),Circle(5),Rectange(20,15),Circle(5),Square(15),Ellipse(10,20)]

def computer_area(shapes):
    s = 0
    for i in range(0,len(shapes)):
        s = s + shapes[i].get_area()
    return s

total_area = computer_area(shapes)
print(total_area)
