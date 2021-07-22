import sys

N = int(input())
x = list(map(int,sys.stdin.readline().split()))
t = sorted(list(set(x)))
result = {t[i] : i for i in range(len(t))}
for i in x: print(result[i], end=' ')
    
'''
import sys, copy

N = int(input())
x = list(map(int,sys.stdin.readline().split()))
result = copy.deepcopy(x)
x = sorted(list(set(x)))
for i in range(N):  result[i] = x.index(result[i])
for i in result: print(i, end=' ')
    
'''