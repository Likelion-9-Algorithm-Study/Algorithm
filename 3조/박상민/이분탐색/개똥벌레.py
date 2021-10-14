# https://www.acmicpc.net/problem/3020
import sys
input = sys.stdin.readline

n, h = map(int, input().split())

top = []
bottom = []

for i in range(n):
    a = int(input().rstrip())
    if i % 2 == 0:
        bottom.append(a)
    else:
        top.append(a)
top.sort()
bottom.sort()

def binary_search(arr, target):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

result = n
count = 0

for i in range(1, h+1):
    bot_count = len(bottom) - binary_search(bottom, i-0.5)
    top_count = len(top) - binary_search(top, h-i+0.5)

    if result == bot_count + top_count:
        count += 1
    elif result > bot_count + top_count:
        count = 1
        result = bot_count + top_count
        # result값을 계속 줄여나가면서 그 때마다 count값을 초기화해준다.(1로)
print(result, count)
