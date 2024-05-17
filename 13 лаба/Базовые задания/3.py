#обычный режим
import time

def Floid(A):
    F = A.copy()
    for k in 'ABC': 
        for i in 'ABC': 
            for j in 'ABC': 
                A[i][j] = min(A[i][j],A[i][k]+A[k][j])
    return F

W = {
    'A': {'A': 0, 'B': 1, 'C': 3, 'D':1, 'E':4},
    'B': {'A': 1, 'B': 0, 'C': 1, 'D':3, 'E':1},
    'C': {'A': 3, 'B': 2, 'C': 0, 'D':7, 'E':2},
    'D': {'A': 4, 'B': 1, 'C': 2, 'D':0, 'E':5},
    'E': {'A': 10, 'B': 1, 'C': 5, 'D':2, 'E':0}
}
t = time.time()
A = W.copy()
print(Floid(A))
print(time.time()-t)

## распараллелить вар 1
import threading
import time

def update_row(A, k, i, j):
    A[i][j] = min(A[i][j], A[i][k] + A[k][j])

def Floid_parallel(A):
    F = A.copy()
    threads = []
    for k in 'ABC':
        for i in 'ABC':
            for j in 'ABC':
                t = threading.Thread(target=update_row, args=(A, k, i, j))
                threads.append(t)
                t.start()
                
    for t in threads:
        t.join()
        
    return F

W = {
    'A': {'A': 0, 'B': 1, 'C': 3, 'D':1, 'E':4},
    'B': {'A': 1, 'B': 0, 'C': 1, 'D':3, 'E':1},
    'C': {'A': 3, 'B': 2, 'C': 0, 'D':7, 'E':2},
    'D': {'A': 4, 'B': 1, 'C': 2, 'D':0, 'E':5},
    'E': {'A': 10, 'B': 1, 'C': 5, 'D':2, 'E':0}
}

t = time.time()
A = W.copy()
print(Floid_parallel(A))
print(time.time()-t)

## распараллелить вар 2

from threading import Thread
import time

W = {
    'A': {'A': 0, 'B': 1, 'C': 3, 'D':1, 'E':4},
    'B': {'A': 1, 'B': 0, 'C': 1, 'D':3, 'E':1},
    'C': {'A': 3, 'B': 2, 'C': 0, 'D':7, 'E':2},
    'D': {'A': 4, 'B': 1, 'C': 2, 'D':0, 'E':5},
    'E': {'A': 10, 'B': 1, 'C': 5, 'D':2, 'E':0}
}

def search_min(k):
    for i in 'ABC':
        for j in 'ABC': 
            A[i][j] = min(A[i][j],A[i][k]+A[k][j])



ta = time.time()
A = W.copy()
threads = [Thread(target=search_min, args=(k,)) for k in 'ABC']
for t in threads:
    t.start()

for t in threads:
    t.join()
print(A)
print(time.time()-ta)