class vector:

    def __init__(self, x, y, z):
        
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other): #– для операции сложения
            return self.x + other.x, self.y + other.y, self.z + other.z

    def __sub__(self, other): #– для операции вычитания
            return self.x - other.x, self.y - other.y, self.z - other.z

    def __mul__(self, other): #– для операции скалярного умножения
            return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self): #– для операции длина вектора
            return ((self.x)**2 + (self.y)**2 + (self.z)**2)**0.5

    def cos(self, other): #– для операции угол между векторами
            return (self.x * other.x + self.y * other.y + self.z * other.z)/(((self.x)**2 + (self.y)**2 + (self.z)**2)**0.5 * ((other.x)**2 + (other.y)**2 + (other.z)**2)**0.5)
    

v1 = vector(2, 3, 4)
v2 = vector(5, 3, 4)
v3 = vector(*(v1+v2))
v4 = vector(*(v1-v2))
res = v1*v2
res2 = v1.length()
res3 = v1.cos(v2)
print(v3, v4, res, res2, res3)