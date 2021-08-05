# 백준 18353번 병사 배치하기 (DP)
# 남는 병사수 최대로, 내림차순은 유지하면서~ 

from sys import stdin
f = stdin.readline
n = int(f())
soldiers = list(map(int, f().split()))

def solution(n, arr):
    answer = 0
    for i in range(n):
        temp = 0
        for j in range(i, n):
            
    
    print(arr3)

    return len(arr3)



print(solution(n, soldiers))