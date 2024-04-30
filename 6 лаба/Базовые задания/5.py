import os

c = False
for (p, d, f) in os.walk("c:\\"):
    for file in f:
        if file == 'Laba 6.ipynb':
            print(str(p)+'\\' + str(file))
            c = True
    if c:
        break