import sys
r = sys.stdin.readline

N = int(r())
K = int(r())

left, right = 1, K

while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for i in range(1, N+1): cnt += min(mid//i, N)
    if cnt < K:
        left = mid + 1
    else:
        result = mid
        right = mid - 1
print(result)




'''
1. 
k번째 수는 k를 넘길 수 없음

2.
4 x 4 행렬
1 2 3 4   - > 4보다 작은 수 4개  4//1
2 4 6 8   - > 4보다 작은 수 2개  4//2
3 6 9 12  - > 4보다 작은 수 1개  4//3
4 8 12 16 - > 4//4 

3.
1 2 3 
2 4 6
3 6 9

1 이하 1개
2 이하 3개
3 이하 5
4 이하 6
5 이하 6 - 4 이하의 수와 변화 없음 = 5 없음
6 이하 8
7 이하 8 - 6 이하의 수와 변화 없음 = 7 없음
8 이하 8
9 이하 9 
'''