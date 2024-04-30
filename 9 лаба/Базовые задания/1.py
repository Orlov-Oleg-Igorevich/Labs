import pylab
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pt

class GeometricShapes:

    def __init__(self, area, perimeter, coordinates):

        self.area = area
        self.perimeter = perimeter
        self.coordinates = coordinates

class triangle(GeometricShapes):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        GeometricShapes.__init__(self, self.area(), self.perimeter(), self.__dict__)
    
    def area(self):
        #S=0,5* (x1-x3) (y2-y3)- (x2-x3) (y1-y3)]
        S = 0.5* (self.a[0]-self.c[0])*(self.b[1]-self.c[1]) - (self.b[0]-self.c[0])*(self.a[1]-self.c[1])
        return abs(S)

    def perimeter(self):
        AB = (self.b[0]-self.a[0], self.b[1]-self.a[1])
        BC = (self.c[0]-self.b[0], self.c[1]-self.b[1])
        AC = (self.c[0]-self.a[0], self.c[1]-self.a[1])
        AB = (AB[0]**2 + AB[1]**2)**0.5
        BC = (BC[0]**2 + BC[1]**2)**0.5
        AC = (AC[0]**2 + AC[1]**2)**0.5
        return AB + BC + AC

    def paint(self):
        x = [self.a[0], self.b[0], self.c[0], self.a[0]]
        y = [self.a[1], self.b[1], self.c[1], self.a[1]]
        plt.plot(x, y)
        plt.show()

class rectangle(GeometricShapes):

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        GeometricShapes.__init__(self, self.area(), self.perimeter(), self.__dict__)
    
    def area(self):
        S = 0.5* abs( (self.a[0]*self.b[1]) + (self.b[0]*self.c[1]) + (self.c[0]*self.d[1]) + (self.d[0]*self.a[1]) -
        (self.b[0]*self.a[1]) - (self.c[0]*self.b[1]) - (self.d[0]*self.c[1]) - (self.a[0]*self.d[1]) )
        return S

    def perimeter(self):
        AB = (self.b[0]-self.a[0], self.b[1]-self.a[1])
        BC = (self.c[0]-self.b[0], self.c[1]-self.b[1])
        CD = (self.d[0]-self.c[0], self.d[1]-self.c[1])
        AD = (self.d[0]-self.a[0], self.d[1]-self.a[1])
        AB = (AB[0]**2 + AB[1]**2)**0.5
        BC = (BC[0]**2 + BC[1]**2)**0.5
        CD = (CD[0]**2 + CD[1]**2)**0.5
        AD = (AD[0]**2 + AD[1]**2)**0.5
        return AB + BC + CD + AD

    def paint(self):
        x = [self.a[0], self.b[0], self.c[0], self.d[0], self.a[0]]
        y = [self.a[1], self.b[1], self.c[1], self.d[1], self.a[1]]
        plt.plot(x, y)
        plt.show()

class circle(GeometricShapes):

    def __init__(self, r, coord):
        self.r = r
        GeometricShapes.__init__(self, self.area(), self.perimeter(), coord)
    
    def area(self):
        S = 3.14*self.r**2
        return S

    def perimeter(self):
        return 2*3.14*self.r

    def paint(self):
        draw_circle = plt.Circle(self.coordinates, self.r, fill=False)
        plt.xlim(xmin=-15,xmax=15)
        plt.ylim(ymin=-15,ymax=15)
        plt.gcf().gca().add_artist(draw_circle)
        plt.show()


t1 = triangle((1, 2), (3, 4), (8, 1))
t3 = circle(5, (3, 4))
t2 = rectangle((1, 1), (1, 4), (5, 4), (5, 1))
t2.paint()