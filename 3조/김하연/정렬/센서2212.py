import sys
f = sys.stdin.readline

n = int(f())
k = int(f())
sensor = sorted(list(map(int, f().split())))
res = sorted([sensor[i] - sensor[i-1] for i in range(1, n)], reverse=True)[k-1:]
print(sum(res))