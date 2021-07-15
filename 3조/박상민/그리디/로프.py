# https://www.acmicpc.net/problem/2217
<<<<<<< HEAD

=======
>>>>>>> ab8c15767510d38a0641453e50ad23b95e5eefd3
import sys

n = int(sys.stdin.readline())
a_list = []
for i in range(n):
    a_list.append(int(sys.stdin.readline()))

a_list.sort(reverse=True)

candidate = list()
for i in range(n):
    candidate.append(a_list[i] * (i+1))

print(max(candidate))
