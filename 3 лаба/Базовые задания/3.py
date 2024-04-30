#a
def ans(x, y):
    a = (y <= -x) or (x > 4 and y > 3)
    return a

x, y = float(input("Введите координату х: ")), float(input("Введите координату y: "))
print(ans(x, y))

#б
def ans(x, y):
    a = (x**2 + y**2 >= 3**2) and (-3 <= x <= 3 and -3 <= y <= 3)
    return a

x, y = float(input("Введите координату х: ")), float(input("Введите координату y: "))
print(ans(x, y))

#в
def ans(x, y):
    a = ((x-5)**2 + (y-5)**2 >= 5**2) and (x >= 0 and y >= 0)
    return a

x, y = float(input("Введите координату х: ")), float(input("Введите координату y: "))
print(ans(x, y))