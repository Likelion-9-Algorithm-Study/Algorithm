n = int(input())
k = int(input())

start = 1
end = k
ans = 0
while start <= end:
    mid = (start+end) // 2
    t = 0
    for i in range(1, n+1):
        t += min(mid//i, n)
    if t >= k:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
print(ans)
# 현재 k는 7
