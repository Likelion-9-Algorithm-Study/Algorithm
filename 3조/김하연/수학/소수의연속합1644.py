import sys
f = sys.stdin.readline

n = int(f())
prime = [False, False] + [True] * (n+1)

for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        for j in range(2*i, n+1, i):
            prime[j] = False

primes = [i for i in range(2, n+1) if prime[i]]

res, start, end = 0, 0, 0

while end <= len(primes):
    temp = sum(primes[start:end])
    if temp == n:
        res += 1
        end += 1
    elif temp > n:
        start += 1
    else:
        end += 1

print(res)