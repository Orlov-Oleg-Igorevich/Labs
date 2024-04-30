nums = list(input("Введите любые сиволы (используйте пробел как разделитель): ").split())
nums = "\n".join(nums)

with open("Символы.txt", 'w') as f:
    f.write(nums)

del nums

nums = []

try:
    file = open("Символы.txt", "r")
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
        try:
            nums.append(float(i))
        except ValueError:
            continue
    
# Прибираемся после себя даже в том случае, если выше возникло исключение
finally:
    file.close()


sum_ = sum(nums)
max_ = max(nums)
min_ = min(nums)

nums  = [str(sum_), str(max_), str(min_)]
nums = "\n".join(nums)

with open("Символы.txt", 'a') as f:
    f.write('\n')
    f.write(nums)