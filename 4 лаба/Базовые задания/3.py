def fib():
    yield 1
    a = 0
    b = 1
    while True:
        yield a + b
        a, b = b, a+b

n = 0
for i in fib():
    n += 1
    x = 1/(5**0.5)*( ((1+5**0.5)/2)**(n) - ((1-5**0.5)/2)**(n) )
    if abs(i-x) > 0.001:
        print(f"Отличие на указанную величину возникло на {n} числе")
        break