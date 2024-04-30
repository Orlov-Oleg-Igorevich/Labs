class Polynomial:

    def __init__(self, degree, coefficients):
        
        self.degree = degree 
        self.coefficients =  coefficients
    
    def __add__(self, other): #– для операции сложения

            if self.degree > other.degree:
                num = self.degree - other.degree
                a = []
                self_coefficients = self.coefficients[num:]
                for i in range(other.degree + 1):
                    a.append(self_coefficients[i] + other.coefficients[i])
                return len(self.coefficients[:num] + a)-1, self.coefficients[:num] + a
            else:
                num = other.degree - self.degree
                a = []
                other_coefficients = other.coefficients[num:]
                for i in range(self.degree + 1):
                    a.append(self.coefficients[i] + other_coefficients[i])
                return len(other.coefficients[:num] + a)-1, other.coefficients[:num] + a

    def __sub__(self, other): #– для операции вычитания

            if self.degree > other.degree:
                num = self.degree - other.degree
                a = []
                self_coefficients = self.coefficients[num:]
                for i in range(other.degree + 1):
                    a.append(self_coefficients[i] - other.coefficients[i])
                return len(self.coefficients[:num] + a)-1, self.coefficients[:num] + a
            else:
                num = other.degree - self.degree
                a = []
                other_coefficients = other.coefficients[num:]
                for i in range(num):
                    a.append(-other.coefficients[i])
                for i in range(self.degree + 1):
                    a.append(self.coefficients[i] - other_coefficients[i])
                return len(a)-1, a

    def __mul__(self, other): #– для операции умножения
        a =  [ [] for i in range(self.degree+1) ]
        for i in range(self.degree+1):
            for j in other.coefficients:
                a[i].append(self.coefficients[i]*j)
        
        s = []
        for i in range(len(a[0])):
            s0 = 0
            s0 += a[0][i]
            x, y = 1, i-1
            while x >= 0 and y >= 0 and x <= (self.degree):
                s0 += a[x][y]
                x, y = x+1, y-1
            s.append(s0)
        
        for i in range(1, self.degree+1):
            s0 = 0
            s0 += a[i][-1]
            x, y = i+1, -2
            while x >= 0 and abs(y) <= (other.degree+1) and x <= (self.degree):
                s0 += a[x][y]
                x, y = x+1, y-1
            s.append(s0)
        return len(s)-1, s


    def __str__(self): #– для вывода
        a = []
        count = 0
        for i in range(self.degree, -1, -1):
            if i != 0 and i != 1 and i != self.degree:
                if self.coefficients[count] < 0:
                    a.append(' - ' + str(self.coefficients[count])[1:] + 'x^' + str(i))
                else:
                     a.append(' + ' + str(self.coefficients[count]) + 'x^' + str(i))
            elif i == self.degree:
                a.append(str(self.coefficients[count]) + 'x^' + str(i))
            elif i == 1:
                if self.coefficients[count] < 0:
                    a.append(' - ' + str(self.coefficients[count])[1:] + 'x')
                else:
                     a.append(' + ' + str(self.coefficients[count]) + 'x')
            else:
                if self.coefficients[count] < 0:
                    a.append(' - ' + str(self.coefficients[count])[1:])
                else:
                     a.append(' + ' + str(self.coefficients[count]))
            count += 1

        return ''.join(a)


f1 = Polynomial(2, [9, 16, 1])
f2 = Polynomial(3, [2, -3, 18, -2])
f3 = Polynomial(*(f1 * f2))
print(f3.coefficients)
print(f3)