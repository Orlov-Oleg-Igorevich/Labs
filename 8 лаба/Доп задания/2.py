class numbers:

    def __init__(self, a, b, i_square):
        
        self.a = a
        self.b = b
        self.i_square = i_square

    def __add__(self, other): #– для операции сложения
            return self.a + other.a, self.b + other.b, self.i_square

    def __sub__(self, other): #– для операции вычитания
            return self.a - other.a, self.b - other.b, self.i_square

    def __mul__(self, other): #– для операции умножения
            return (self.a*other.a + self.b*other.b*self.i_square), (self.b*other.a + self.a*other.b), self.i_square

    def __truediv__(self, other): #– для операции деления
             return round((self.a*other.a + self.b*other.b)/(other.a**2 + other.b**2), 3), round((self.b*other.a - self.a*other.b)/(other.a**2 + other.b**2), 3), self.i_square


v1 = numbers(2, 3, -1)
v2 = numbers(5, -7, -1)
v1 / v2