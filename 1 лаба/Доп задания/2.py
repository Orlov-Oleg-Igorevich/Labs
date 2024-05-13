x = int(input("введите целое число: "))
while x > 9:
    x = sum(int(i) for i in str(x))
    print(x)