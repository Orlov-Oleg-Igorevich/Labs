x = input("Введите число x: ")

a = (len(x) == 3 and x[-1] == 0) + (int(float(x))%2!=0 and (int(float(x))%3==0 or int(float(x))%5==0)) + (2 <= float(x) <= 6) + (len(x) == 3 and x.count(x[0])==len(x))

print(bool(a))