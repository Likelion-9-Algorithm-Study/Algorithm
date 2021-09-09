import sys, heapq
f = sys.stdin.readline

n = int(f())
num = []
for _ in range(n):
    num.append(int(f()))
heapq.heapify(num)
res = 0

while len(num) > 1:
    a = heapq.heappop(num)
    b = heapq.heappop(num)
    heapq.heappush(num, a+b)
    res += a+b

print(res)

