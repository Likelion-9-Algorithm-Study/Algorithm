import sys

r = sys.stdin.readline

N, C = map(int, r().split())
x = []
for i in range(N):
    x.append(int(r()))
x.sort()


def router():
    start, end, result = 1, x[-1] - x[0], 0

    while start <= end:
        gap = (start + end) // 2
        current, cnt = x[0], 1
        for i in range(1, N):
            if x[i] >= current + gap:
                cnt += 1
                current = x[i]
        if cnt >= C:
            start = gap + 1
            result = gap
        else:
            end = gap - 1
    return result


print(router())
