import sys
r = sys.stdin.readline

N = int(r())
food = list(map(int, r().split()))

result = [0] * (N+1)

result[0], result[1] = food[0], food[1]

for i in range(2, N):
    result[i] += max(result[i-1], result[i-2]+food[i])
print(result[N-1])

'''
for i in range(2, N):
    food[i] += max(food[:i-1])

print(food[N-1])
'''