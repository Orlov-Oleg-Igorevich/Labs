def convert_base (num, to_base=10, from_base=10):
    
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
        x = int (num, from_base)             
    
        it = 0
        digit = []
    
        while x>0:
                    digit.insert(0, alphabet[x % to_base])
                    x = x // to_base
                    it+=1
        
        return ''.join(digit)

n = int(input("Введите сс, в которой будут происходить вычисления: "))
a, b = input("Введите первое число: "), input("Введите второе число: ")
hum = int(input('''Выберите тип операции(введите номер):
        1. *
        2. +
        3. //
        4. -'''))

if hum == 1:
        ans = int(a, n)*int(b, n)
        print(f"{a} умножить на {b} равно {convert_base(str(ans), n)}")
elif hum == 2:
        ans = int(a, n)+int(b, n)
        print(f"{a} + {b} равно {convert_base(str(ans), n)}")
elif hum == 3:
        ans = int(a, n)//int(b, n)
        print(f"{a} / {b} равно {convert_base(str(ans), n)}")
else:
        ans = int(a, n)-int(b, n)
        print(f"{a} - {b} равно {convert_base(str(ans), n)}")
