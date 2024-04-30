def dev_for(n):
    if n%2 == 0: return 2
    for i in range(3, int(n**0.5)+1):
        if n%i == 0:
            return i
    else: return n

def dev_while(n):
    if n%2 == 0: return 2
    i = 3
    while i**2 <= n:
        if n%i == 0:
            return i
        i += 1
    else: return n

n = int(input('Введите целое число, не меньше двух: '))

print(dev_for(n), dev_while(n))
