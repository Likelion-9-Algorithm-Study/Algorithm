import sys
r = sys.stdin.readline

N = int(r())
store = list(map(int, r().split()))
M = int(r())
client = list(map(int, r().split()))

store.sort()

for i in range(M):
    key = client[i]
    left, right = 0, N-1
    while left <= right:
        mid = (left + right)//2
        current = store[mid]
        if current == key:
            print('yes', end=' ')
            break
        elif current > key:
            right = mid - 1
        else:
            left = mid + 1
    else:
        print('no', end=' ')
