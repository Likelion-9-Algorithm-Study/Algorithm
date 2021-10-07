import sys
from collections import Counter
f = sys.stdin.readline

r, c, k=map(int, f().split())
A = [list(map(int, f().split())) for _ in range(3)]

r, c, time = r-1, c-1, 0
while time<=100:
    if r < len(A) and c < len(A[0]) and A[r][c] == k:
        print(time)
        break

    C_flag = False
    if len(A) < len(A[0]):
        C_flag = True
        A = list(zip(*A))

    max_len = 0
    temp = []
    for cr in A:
        ct = Counter(cr)
        if ct.get(0): del ct[0]
        num_cnt = list(map(list, ct.items()))
        num_cnt.sort(key=lambda x: (x[1], x[0]))
        temp.append(list(sum(num_cnt, []))[:100])
        max_len = max(max_len, len(temp[-1]))

    for i in range(len(temp)):
        if len(temp[i]) < max_len:
            temp[i] += [0]*(max_len-len(temp[i]))

    A = temp
    if C_flag:
        A = list(zip(*A))
    time += 1

if time>100:
    print(-1)