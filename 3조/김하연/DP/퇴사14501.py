import sys
r = sys.stdin.readline

N = int(r())
T, P = [], []

for i in range(N):
    t, p = map(int, r().split())
    T.append(t)
    P.append(p)

result = [0] * (N+1)

for i in range(N-1, -1, -1):
    if i + T[i] > N:
        result[i] = result[i+1]
    else:
        result[i] = max((P[i] + result[i + T[i]]), result[i+1])

print(result[0])
