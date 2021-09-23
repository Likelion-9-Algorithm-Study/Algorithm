import sys
from collections import deque
f = sys.stdin.readline


def prime():
    for i in range(2, 100):
        if primes[i]:
            for j in range(2*i, 10000, i):
                primes[j] = False


def bfs(s, d):
    q = deque([(s, 0)])
    visited = [0 for _ in range(10000)]
    visited[s] = 1

    while q:
        cur, cnt = q.popleft()
        cur = str(cur)
        if cur == d:
            return cnt
        for i in range(4):
            for j in range(10):
                temp = int(cur[:i] + str(j) + cur[i+1:])
                if not visited[temp] and primes[temp] and temp >= 1000:
                    visited[temp] = 1
                    q.append((temp, cnt+1))


t = int(f())
primes = [True for _ in range(10000)]
prime()
for _ in range(t):
    start, dest = map(int, f().split())
    res = bfs(start, str(dest))
    print(res if res != None else 'Impossible')
