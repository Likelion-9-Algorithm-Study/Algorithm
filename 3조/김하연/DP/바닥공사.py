N = int(input())

result = [0] * (N+1)
result[1], result[2] = 1, 3

for i in range(3, N+1):
    result[i] += (result[i-1] + 2 * result[i-2]) % 796796

print(result[N])
