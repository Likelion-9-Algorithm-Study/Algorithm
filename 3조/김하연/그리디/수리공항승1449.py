import sys
n, l = map(int,input().split())
leak = list(map(int,sys.stdin.readline().split()))
leak.sort()
tape, current = 1, leak[0]
for i in range(1,n):
    if leak[i] - current + 1 > l:
        tape+=1
        current = leak[i]
print(tape)
