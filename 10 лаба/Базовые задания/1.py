def search(k):
    with open("pi-10million.txt") as f:
        count = 1
        st = f.read(len(k)+1)
        while st[1:] != k:
            st = st[1:] + f.read(1)
            count += 1
            if count == 10_000_000:
                print("Не найдено")
                break
        
    return count

print(search('999999'))
print(search('888888'))
print(search('000000'))
print(search('1234567'))
print(search('9756440'))