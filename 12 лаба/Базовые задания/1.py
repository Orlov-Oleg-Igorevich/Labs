def search(n):
    f = [0 for i in range(n+1)]
    f[1] = 1
    for i in range(2, n+1):
        if i%3 == 0:
            f[i] = f[i//3] + f[i-1] + f[i-2]
        else:
            f[i] = f[i-1] + f[i-2]
    return f[n]

search(22)