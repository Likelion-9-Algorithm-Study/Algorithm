import sys

N = int(sys.stdin.readline())


def solution():
    if N == 1:
        return 0
    elif N == 2 or N == 3:
        return 1

    num = [1] * (N + 1)

    for i in range(4, N+1):
        temp1 = num[i // 3] if i % 3 == 0 else sys.maxsize
        temp2 = num[i // 2] if i % 2 == 0 else sys.maxsize
        temp3 = num[i - 1]

        num[i] += min(temp1, temp2, temp3)

    return num[N]


print(solution())
