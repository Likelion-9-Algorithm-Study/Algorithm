import sys
r = sys.stdin.readline

N, M = map(int, r().split())
coin = []
for i in range(N):
    coin.append(int(r()))
result = [20000] * (max(max(coin), M)+1)
for x in coin:  result[x] = 1

for i in range(M+1):
    for x in coin:
        if x <= i:
            result[i] = min(result[i], result[i-x]+1)

if result[M] == 20000: print(-1)
else: print(result[M])

# for i in range(N):
#     for j in range(coin[i], M+1):
#         if result[j - coin[i]] != 20000:
#             result[j] = min(result[j], result[j - coin[i]] + 1)
#
# if result[M] == 20000: print(-1)
# else: print(result[M])
