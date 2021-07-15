# https://www.acmicpc.net/problem/14241
<<<<<<< HEAD

=======
>>>>>>> ab8c15767510d38a0641453e50ad23b95e5eefd3
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

a.sort(reverse=True)
i = 0
total_score = 0
while len(a) != 1:
    total_score += a[i] * a[i+1]
    a[i] += a[i+1]
    del(a[i+1])

print(total_score)
