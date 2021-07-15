# https://www.acmicpc.net/problem/18406
score = input()
mid = len(score) // 2
left, right = [0] * mid, [0] * mid
for i in range(mid):
    left[i] = int(score[i])
for i in range(mid, len(score)):
    right[i-mid] = int(score[i])

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")
