def rotate_a_martix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for i in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def check(lock):
    length = len(lock)//3
    for i in range(length, length*2):
        for j in range(length, length*2):
            if lock[i][j]!=1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n*3) for i in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for r in range(4): # rotation
        key = rotate_a_martix_by_90_degree(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[i+x][j+y] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[i+x][j+y] -= key[i][j]
    return False
            