class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0


    def calc_area(self):
        return self.b * self.h /2



x = Triangulo()
print(x)
y = x
print(y)
y.b = 10
print(x.b)