import sys
n = int(input())
t = list(map(int,sys.stdin.readline().split()))

t.sort(reverse=True)
for i in range(n):
    t[i]+=i
print(max(t)+2) # 심는 날 하루 + 다 심고난 다음날 하루 = 2일 더하기