import copy
import numpy as np

#код из задания 3 предыдущей лабы
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


class Matrix:

    def __init__(self, list_):
        self.value = self.copy(list_)

    def transposed(self):
        return Matrix(np.transpose(np.array(self.value)))

    def __add__(self, other):
        if self.size() == other.size():
            return Matrix(list(np.array(self.value) + np.array(other.value)))
        else: print("Данные матрицы нельзя сложить")

    def __mul__(self, other):
        if type(other) == Matrix and self.size()[1] == other.size()[0]:
            return Matrix(list(np.array(self.value) * np.array(other.value)))
        elif type(other) == int:
            return Matrix(list(np.array(self.value) * other))
        else: print("Невозможно провести даннцю операцию")

    __rmul__ = __mul__


    def size(self):
        return (len(self.value), len(self.value[0]))

    def __str__(self):
        a = ['    '.join(map(str, i)) for i in self.value]
        a = '\n'.join(a)
        return a

    def copy(self, list_):
        return copy.deepcopy(list_)


class Vector(Matrix, vector):

    def __init__(self, value):
        Matrix.__init__(self, value)
        vector.__init__(self, *value)

    def vector_product(self, other):
        return Vector([self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x])

    def __str__(self):
        return '    '.join(map(str, self.value))

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(v1.vector_product(v2))