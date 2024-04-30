nums = list(input("Введите вещественные числа (используйте пробел как разделитель): ").split())
nums = "\n".join(nums)

with open("Числа.txt", 'w') as f:
    f.write(nums)

del nums


nums = []

try:
    file = open("Числа.txt", "r")
    print("Файл успешно открыт!")
except FileNotFoundError:
    # Обработка ошибки, возникающей в том случае, если файл не найден
    print("Файл не найден!")
    exit()
except PermissionError:
    # Обработка ошибок, связанных с разрешением на доступ к файлу
    print("Ошибка доступа!")
else:
    for i in file:
        nums.append(float(i))
    
# Прибираемся после себя даже в том случае, если выше возникло исключение
finally:
    file.close()


sum_ = sum(nums)
max_ = max(nums)
min_ = min(nums)

nums  = [str(sum_), str(max_), str(min_)]
nums = "\n".join(nums)

with open("Числа.txt", 'a') as f:
    f.write('\n')
    f.write(nums)