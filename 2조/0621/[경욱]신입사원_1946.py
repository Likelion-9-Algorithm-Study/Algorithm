import sys


def sol(n):
    result = []
    temp_list = [list(map(int, sys.stdin.readline().split()))
                 for _ in range(n)]
    temp_list = sorted(temp_list, key=lambda x: x[0])

    top = float('inf')
    for i in range(len(temp_list)):
        temp = temp_list[i]
        if temp[1] > top:
            continue
        elif temp[1] < top:
            top = temp[1]
            result.append(temp)

    print(len(result))
    return


t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    sol(n)
