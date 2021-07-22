import sys
input = sys.stdin.readline
N, K = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(K):
    if a[i] < b[i]: a[i] = b[i]
    else: break

print(sum(a))