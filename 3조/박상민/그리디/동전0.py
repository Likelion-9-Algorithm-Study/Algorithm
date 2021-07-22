# https://www.acmicpc.net/problem/11047
<<<<<<< HEAD

=======
>>>>>>> ab8c15767510d38a0641453e50ad23b95e5eefd3
import sys

n, k = list(map(int, sys.stdin.readline().split()))

coin_list = []
for _ in range(n):
    coin_list.append(int(sys.stdin.readline()))

coin_list.sort(reverse=True)

count = 0
for i in coin_list:
    count += k // i
    k %= i

print(count)
