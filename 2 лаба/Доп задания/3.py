N = int(input("Введите число N: "))
q = list(range(1, N+1))

while q:
    ans = int(input(f'''Ваше число: /n
    1. > {q[int(len(q))//2-1]}
    2. < {q[int(len(q))//2-1]} 
    3. = {q[int(len(q))//2-1]}
    Введите номер верного утверждени: '''))
    q_last = q
    if ans == 1:
        a = int(len(q))//2
        q = q[a:]
    elif ans == 2:
        b = int(len(q))//2-1
        q = q[:b]
    elif ans == 3:
        print(f'Загаданное число: {q[len(q)//2-1]}')
        break
else:
    if ans == 1:
        print(q_last[int(len(q))//2-1]+1)
    else:
        print(q_last[int(len(q))//2-1]-1)