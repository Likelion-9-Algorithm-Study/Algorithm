import sys
r = sys.stdin.readline

N = int(r())
soldier = list(map(int, r().split()))

result = [1] * N
for i in range(N):
    for j in range(i):
        if soldier[i] < soldier[j]:
            result[i] = max(result[i], result[j]+1)

print(N - max(result))
