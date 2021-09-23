import sys
from math import gcd
f = sys.stdin.readline

n = int(f())
num = sorted(list(int(f()) for _ in range(n)))
subs, result = [], set()

for i in range(1, n):
    subs.append(num[i] - num[i-1])

temp = subs[0]
for i in range(1, len(subs)):
    temp = gcd(temp, subs[i])

result.add(temp)
for i in range(2, int(temp ** 0.5) + 1):
    if temp % i == 0:
        result.add(i)
        result.add(temp // i)

result = sorted(list(result))
print(*result)
