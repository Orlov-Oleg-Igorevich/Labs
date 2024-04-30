class parameters:

    def __init__(self, value, description):
        self.value = value
        self.description = description

#первый вариант реализации
class calculations:

    @staticmethod 
    def area_triangle(a, b, c):
        #S=0,5* (x1-x3) (y2-y3)- (x2-x3) (y1-y3)]
        S = 0.5* (a[0]-c[0])*(b[1]-c[1]) - (b[0]-c[0])*(a[1]-c[1])
        return abs(S)

    @staticmethod 
    def perimeter_triangle(a, b, c):
        AB = (b[0]-a[0], b[1]-a[1])
        BC = (c[0]-b[0], c[1]-b[1])
        AC = (c[0]-a[0], c[1]-a[1])
        AB = (AB[0]**2 + AB[1]**2)**0.5
        BC = (BC[0]**2 + BC[1]**2)**0.5
        AC = (AC[0]**2 + AC[1]**2)**0.5
        return AB + BC + AC

    @staticmethod 
    def area_rectangle(a, b, c, d):
        S = 0.5* abs( (a[0]*b[1]) + (b[0]*c[1]) + (c[0]*d[1]) + (d[0]*a[1]) -
        (b[0]*a[1]) - (c[0]*b[1]) - (d[0]*c[1]) - (a[0]*d[1]) )
        return S

    @staticmethod 
    def perimeter_rectangle(a, b, c, d):
        AB = (b[0]-a[0], b[1]-a[1])
        BC = (c[0]-b[0], c[1]-b[1])
        CD = (d[0]-c[0], d[1]-c[1])
        AD = (d[0]-a[0], d[1]-a[1])
        AB = (AB[0]**2 + AB[1]**2)**0.5
        BC = (BC[0]**2 + BC[1]**2)**0.5
        CD = (CD[0]**2 + CD[1]**2)**0.5
        AD = (AD[0]**2 + AD[1]**2)**0.5
        return AB + BC + CD + AD

    @staticmethod 
    def area_circle(r):
        S = 3.14*r**2
        return S

    @staticmethod 
    def perimeter_circle(r):
        return 2*3.14*r


#второй вариатн реализации
class CalculationOFParameters:

    def area_triangle(a, b, c):
        figure = triangle(a, b, c)
        figure.area()

    def perimeter_triangle(a, b, c):
        figure = triangle(a, b, c)
        figure.perimeter()

    def area_rectangle(a, b, c, d):
        figure = rectangle(a, b, c, d)
        figure.area()

    def perimeter_rectangle(a, b, c, d):
        figure = rectangle(a, b, c, d)
        figure.perimeter()

    def area_circle(r, coord):
        figure = rectangle(r, coord)
        figure.area()
 
    def perimeter_circle(r, coord):
        figure = rectangle(r, coord)
        figure.perimeter()
    

class GeometricShapes:

    def __init__(self, area, perimeter, coordinates):

        self.area = parameters(*area)
        self.perimeter = parameters(*perimeter)
        self.coordinates = parameters(*coordinates)


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