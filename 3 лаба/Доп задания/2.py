str_ = input("Введите вашу строку: ")

srt_ = str_.replace(' ', '')
str_set = set()
ans = ''

for i in srt_:
    if i not in str_set:
        ans += i
        str_set.add(i)

print(ans)
