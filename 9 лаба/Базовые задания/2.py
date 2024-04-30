import copy
import numpy as np

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


c = [[1, 2], [3, 4]]
v = [[1, 2], [3, 4]]
t1 = Matrix(c)
t2 = Matrix(v)
print(3*t1)