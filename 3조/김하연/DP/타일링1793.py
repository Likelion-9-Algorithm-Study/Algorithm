import sys
r = sys.stdin.readline

while True:
    n = r().strip()
    if n != '':
        n = int(n)
        if n == 0 or n == 1: print(1)
        elif n == 2: print(3)
        else:
            result = [0] * (n + 1)
            result[1], result[2] = 1, 3

            for i in range(3, n + 1):
                result[i] += (result[i - 1] + 2 * result[i - 2])

            print(result[n])
    else:
        break
