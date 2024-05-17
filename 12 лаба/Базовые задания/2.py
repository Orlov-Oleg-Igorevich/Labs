def search3(A, B):
    n = len(A)
    m = len(B)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    result = ""
    i, j = n, m
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            result = A[i - 1] + result
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return result
    
A = 'abcabaac'
B = 'baccbca'
print(search3(A, B))