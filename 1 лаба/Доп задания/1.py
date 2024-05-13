import math
import matplotlib.pyplot as plt
import numpy as np


g = 9.80665
v0 = 5
a = 40

y_max = round((v0**2*math.sin(math.radians(a))/(2*g)), 2)
x_max = round((v0**2*math.sin(math.radians(2*a))/g), 2)
del a, v0
print("Максимальная дальность прыжка:", x_max, "м")
print("Максимальная высота прыжка:", y_max, "м")
print()
print("Оптимальный угол для максимальной дальности прыжка: 45" ) # Это элементарно
print()
print("Оптимальный угол для максимальной высоты прыжка: 90" ) # Это элементарно
print()
#x = v0*math.cos(math.radians(a))*t
#y = v0*math.sin(math.radians(a))*t - 1/2*g*t**2
x = 2
y = 3
t = 1

v0cos = x/t
v0sin = (y + 1/2*g*t**2)/t
v0 = (v0cos**2 + v0sin**2)**0.5

print("Нач скорость для попадания в точку (2, 3):", v0)
print("Нач угол для попадания в точку (2, 3):", math.degrees(math.acos(v0cos/v0)))

# c matplotlib
x = 2
y = 3
t = 1
g = 9.80665

v0cos = x/t
v0sin = (y + 1/2*g*t**2)/t
v0 = (v0cos**2 + v0sin**2)**0.5
a = math.acos(v0cos/v0)

del t, v0cos, v0sin, x, y
#x = v0*math.cos(math.radians(a))*t
#y = v0*math.sin(math.radians(a))*t - 1/2*g*t**2

cord_x = [0]
cord_y = [0]

for t in np.arange(0, 2, 0.1):
    x = v0*math.cos(a)*t
    y = v0*math.sin(a)*t - 1/2*g*t**2
    if y > 0:
        cord_y.append(y)
        cord_x.append(x)

plt.plot(cord_x, cord_y)
plt.xlabel('Ось х') 
plt.ylabel('Ось y')
plt.title('График траектории')
plt.show()