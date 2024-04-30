class A:
    variable1 = 1
    variable2 = 2

    @staticmethod
    def look():
        return f'variable1 = {A.variable1}, variable2 = {A.variable2}'

    @staticmethod
    def change(v1, v2):
        A.variable1 =  v1
        A.variable2 = v2

    @staticmethod
    def sum():
        return A.variable1 + A.variable2

    @staticmethod
    def max():
        return max(A.variable1, A.variable2)

A.change(4, 5)
print(A.look())
print(A.sum())
print(A.max())